#!/usr/bin/env python3
from __future__ import annotations

import base64
import ctypes
import datetime
import json
import os
import queue
import traceback
import sys
import threading
from dataclasses import dataclass
from pathlib import Path
from tkinter import BooleanVar, DoubleVar, IntVar, StringVar, Tk, filedialog, messagebox, ttk
import tkinter as tk
try:
    import windnd
except ImportError:
    windnd = None

from batch_generate_storyboards import (
    DEFAULT_AGENT_REVIEW_ENABLED,
    DEFAULT_AGENT_REVIEW_ROUNDS,
    DEFAULT_EPISODES_PER_REQUEST,
    DEFAULT_GENERATION_REASONING_EFFORT,
    DEFAULT_REVIEW_THINKING_ENABLED,
    DEFAULT_REVIEW_REASONING_EFFORT,
    DEFAULT_STABLE_SEGMENT_MODE,
    MAX_EPISODES_PER_REQUEST,
    DEFAULT_SPLIT_DIR_NAME,
    DEFAULT_PROVIDER,
    PROVIDER_CONFIGS,
    PROVIDER_BLTCY_CHAT,
    PROVIDER_DEEPSEEK,
    PROVIDER_QWEN_CHAT,
    build_episode_inputs,
    build_episode_inputs_from_paths,
    find_prompt_file,
    get_provider_api_key_label,
    get_provider_model_options,
    get_provider_reasoning_effort_options,
    is_prompt_like_file,
    log_generation_plan,
    make_output_path,
    normalize_reasoning_effort,
    provider_supports_thinking,
    provider_supports_reasoning_effort,
    read_utf8_text,
    resolve_api_base,
    resolve_default_max_tokens_for_model,
    resolve_model,
    run_batch_generation,
    sanitize_filename_part,
    split_episode_collection_file,
    load_review_skill_text,
    validate_api_key_for_provider,
)


APP_NAME = "Auto-Storyboard Generator"
DEFAULT_MODEL = resolve_model(DEFAULT_PROVIDER)
DEFAULT_API_BASE = resolve_api_base(DEFAULT_PROVIDER)
DEFAULT_OUTPUT_DIR = "outputs"
DEFAULT_MAX_TOKENS = resolve_default_max_tokens_for_model(DEFAULT_PROVIDER, DEFAULT_MODEL)
DEFAULT_TIMEOUT_SECONDS = 1800
DEFAULT_TEMPERATURE = 0.3
DEFAULT_DELAY_SECONDS = 1.0
DEFAULT_MAX_RETRIES = 3
DEFAULT_PARALLELISM = 3
PROVIDER_OPTIONS = [PROVIDER_DEEPSEEK, PROVIDER_QWEN_CHAT, PROVIDER_BLTCY_CHAT]


class DATA_BLOB(ctypes.Structure):
    _fields_ = [("cbData", ctypes.c_uint32), ("pbData", ctypes.POINTER(ctypes.c_ubyte))]


CRYPTPROTECT_UI_FORBIDDEN = 0x1
kernel32 = ctypes.windll.kernel32
crypt32 = ctypes.windll.crypt32


def normalize_paths(paths: list[Path]) -> list[Path]:
    unique: dict[str, Path] = {}
    for path in paths:
        try:
            resolved = path.expanduser().resolve()
        except Exception:
            resolved = path.expanduser()
        unique[str(resolved).lower()] = resolved
    return sorted(unique.values())


def common_parent(paths: list[Path]) -> Path | None:
    if not paths:
        return None
    normalized_roots: list[str] = []
    for path in paths:
        container = path if path.is_dir() else path.parent
        normalized_roots.append(str(container))
    return Path(os.path.commonpath(normalized_roots))


def pick_prompt_file(files: list[Path]) -> Path | None:
    prompt_candidates = [path for path in files if is_prompt_like_file(path)]
    if not prompt_candidates:
        return None
    prioritized = sorted(
        prompt_candidates,
        key=lambda path: ("prompt" not in path.name.lower(), len(path.name), path.name.lower()),
    )
    return prioritized[0]


def app_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


SETTINGS_PATH = app_dir() / "storyboard-gui.settings.json"
APP_LOG_PATH = app_dir() / "storyboard-gui.log"
RUN_LOGS_DIRNAME = "logs"


def append_app_log(message: str) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with APP_LOG_PATH.open("a", encoding="utf-8") as handle:
            handle.write(f"[{timestamp}] {message}\n")
    except Exception:
        pass


def _bytes_to_blob(data: bytes) -> DATA_BLOB:
    if not data:
        return DATA_BLOB(0, None)
    buffer = (ctypes.c_ubyte * len(data)).from_buffer_copy(data)
    return DATA_BLOB(len(data), ctypes.cast(buffer, ctypes.POINTER(ctypes.c_ubyte)))


def _blob_to_bytes(blob: DATA_BLOB) -> bytes:
    if not blob.cbData or not blob.pbData:
        return b""
    return ctypes.string_at(blob.pbData, blob.cbData)


def protect_secret(secret: str) -> str:
    if not secret:
        return ""
    data = secret.encode("utf-8")
    in_blob = _bytes_to_blob(data)
    out_blob = DATA_BLOB()
    if not crypt32.CryptProtectData(
        ctypes.byref(in_blob),
        None,
        None,
        None,
        None,
        CRYPTPROTECT_UI_FORBIDDEN,
        ctypes.byref(out_blob),
    ):
        raise ctypes.WinError()
    try:
        return base64.b64encode(_blob_to_bytes(out_blob)).decode("ascii")
    finally:
        if out_blob.pbData:
            kernel32.LocalFree(out_blob.pbData)


def unprotect_secret(cipher_text: str) -> str:
    if not cipher_text:
        return ""
    raw = base64.b64decode(cipher_text.encode("ascii"))
    in_blob = _bytes_to_blob(raw)
    out_blob = DATA_BLOB()
    if not crypt32.CryptUnprotectData(
        ctypes.byref(in_blob),
        None,
        None,
        None,
        None,
        CRYPTPROTECT_UI_FORBIDDEN,
        ctypes.byref(out_blob),
    ):
        raise ctypes.WinError()
    try:
        return _blob_to_bytes(out_blob).decode("utf-8")
    finally:
        if out_blob.pbData:
            kernel32.LocalFree(out_blob.pbData)


@dataclass
class EpisodeRow:
    index: int
    display_name: str
    episode_number: int | None
    source_name: str
    output_name: str
    char_count: int


class StoryboardApp:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry("1320x900")
        self.root.minsize(1220, 840)

        self.project_var = StringVar()
        self.prompt_var = StringVar()
        self.output_var = StringVar()
        self.api_key_var = StringVar()
        self.provider_var = StringVar(value=DEFAULT_PROVIDER)
        self.model_var = StringVar(value=DEFAULT_MODEL)
        self.api_base_var = StringVar(value=DEFAULT_API_BASE)
        self.generation_thinking_var = BooleanVar(value=True)
        self.review_thinking_var = BooleanVar(value=DEFAULT_REVIEW_THINKING_ENABLED)
        self.generation_reasoning_effort_var = StringVar(value=DEFAULT_GENERATION_REASONING_EFFORT)
        self.review_reasoning_effort_var = StringVar(value=DEFAULT_REVIEW_REASONING_EFFORT)
        self.overwrite_var = BooleanVar(value=False)
        self.agent_review_var = BooleanVar(value=DEFAULT_AGENT_REVIEW_ENABLED)
        self.stable_segment_mode_var = BooleanVar(value=True)
        self.temperature_var = DoubleVar(value=DEFAULT_TEMPERATURE)
        self.timeout_var = IntVar(value=DEFAULT_TIMEOUT_SECONDS)
        self.max_tokens_var = IntVar(value=DEFAULT_MAX_TOKENS)
        self.delay_var = DoubleVar(value=DEFAULT_DELAY_SECONDS)
        self.max_retries_var = IntVar(value=DEFAULT_MAX_RETRIES)
        self.parallelism_var = IntVar(value=DEFAULT_PARALLELISM)
        self.episodes_per_request_var = IntVar(value=DEFAULT_EPISODES_PER_REQUEST)
        self.review_rounds_var = IntVar(value=DEFAULT_AGENT_REVIEW_ROUNDS)
        self._last_recommended_max_tokens = DEFAULT_MAX_TOKENS
        self.status_var = StringVar(value="状态：等待扫描")
        self.progress_var = IntVar(value=0)

        self.episodes = []
        self.selected_script_paths: list[Path] | None = None
        self.tree_row_paths: dict[str, Path] = {}
        self.worker_thread: threading.Thread | None = None
        self.log_queue: queue.Queue[tuple[str, object]] = queue.Queue()
        self.active_run_log_path: Path | None = None
        self.last_run_log_path: Path | None = None

        self._load_settings()
        self._build_ui()
        self.model_var.trace_add("write", self._on_model_name_changed)
        self.generation_thinking_var.trace_add("write", self._on_thinking_changed)
        self.review_thinking_var.trace_add("write", self._on_thinking_changed)
        self._sync_provider_ui()
        self._init_drag_drop()
        self.root.report_callback_exception = self._report_callback_exception
        self.root.after(150, self._drain_queue)
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _build_ui(self) -> None:
        self.root.columnconfigure(1, weight=1)

        main = ttk.Frame(self.root, padding=12)
        main.pack(fill="both", expand=True)
        main.columnconfigure(1, weight=1)

        self._labeled_entry(main, "项目目录", 0, self.project_var, self._choose_project)
        self._labeled_entry(main, "提示词文件", 1, self.prompt_var, self._choose_prompt)
        self._labeled_entry(main, "输出目录", 2, self.output_var, self._choose_output)

        row3 = ttk.Frame(main)
        row3.grid(row=3, column=0, columnspan=3, sticky="ew", pady=(8, 0))
        row3.columnconfigure(3, weight=1)
        row3.columnconfigure(7, weight=1)

        ttk.Label(row3, text="供应商").grid(row=0, column=0, sticky="w")
        provider_combo = ttk.Combobox(
            row3,
            textvariable=self.provider_var,
            values=PROVIDER_OPTIONS,
            state="readonly",
            width=12,
        )
        provider_combo.grid(row=0, column=1, sticky="w", padx=(10, 12))
        provider_combo.bind("<<ComboboxSelected>>", self._on_provider_changed)

        self.api_key_label = ttk.Label(row3, text="API Key")
        self.api_key_label.grid(row=0, column=2, sticky="w")
        self.api_key_entry = ttk.Entry(row3, textvariable=self.api_key_var, show="*")
        self.api_key_entry.grid(row=0, column=3, sticky="ew", padx=(10, 12))

        ttk.Label(row3, text="模型").grid(row=0, column=4, sticky="w")
        self.model_combo = ttk.Combobox(row3, textvariable=self.model_var, width=22)
        self.model_combo.grid(row=0, column=5, sticky="w", padx=(10, 12))

        ttk.Label(row3, text="API").grid(row=0, column=6, sticky="w")
        ttk.Entry(row3, textvariable=self.api_base_var, width=32).grid(row=0, column=7, sticky="ew", padx=(10, 0))

        options_frame = ttk.LabelFrame(main, text="生成参数", padding=(10, 8))
        options_frame.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(8, 0))
        options_frame.columnconfigure(0, weight=1)

        row4_top = ttk.Frame(options_frame)
        row4_top.grid(row=0, column=0, sticky="ew")
        for idx in range(14):
            row4_top.columnconfigure(idx, weight=1 if idx in {1, 3, 5, 7, 9, 11, 13} else 0)

        ttk.Label(row4_top, text="Temperature").grid(row=0, column=0, sticky="w")
        ttk.Spinbox(
            row4_top,
            from_=0.0,
            to=2.0,
            increment=0.1,
            textvariable=self.temperature_var,
            width=8,
        ).grid(row=0, column=1, sticky="w", padx=(8, 18))
        ttk.Label(row4_top, text="Max Tokens").grid(row=0, column=2, sticky="w")
        ttk.Spinbox(
            row4_top,
            from_=1000,
            to=393216,
            increment=500,
            textvariable=self.max_tokens_var,
            width=9,
        ).grid(row=0, column=3, sticky="w", padx=(8, 18))
        ttk.Label(row4_top, text="超时秒数").grid(row=0, column=4, sticky="w")
        ttk.Spinbox(
            row4_top,
            from_=60,
            to=7200,
            increment=60,
            textvariable=self.timeout_var,
            width=8,
        ).grid(row=0, column=5, sticky="w", padx=(8, 18))
        ttk.Label(row4_top, text="延迟秒数").grid(row=0, column=6, sticky="w")
        ttk.Spinbox(
            row4_top,
            from_=0.0,
            to=10.0,
            increment=0.5,
            textvariable=self.delay_var,
            width=8,
        ).grid(row=0, column=7, sticky="w", padx=(8, 18))
        ttk.Label(row4_top, text="重试次数").grid(row=0, column=8, sticky="w")
        ttk.Spinbox(
            row4_top,
            from_=1,
            to=10,
            increment=1,
            textvariable=self.max_retries_var,
            width=6,
        ).grid(row=0, column=9, sticky="w", padx=(8, 18))
        ttk.Label(row4_top, text="并发数").grid(row=0, column=10, sticky="w")
        ttk.Spinbox(
            row4_top,
            from_=1,
            to=10,
            increment=1,
            textvariable=self.parallelism_var,
            width=6,
        ).grid(row=0, column=11, sticky="w", padx=(8, 18))
        ttk.Label(row4_top, text="单次集数").grid(row=0, column=12, sticky="w")
        ttk.Spinbox(
            row4_top,
            from_=1,
            to=MAX_EPISODES_PER_REQUEST,
            increment=1,
            textvariable=self.episodes_per_request_var,
            width=6,
        ).grid(row=0, column=13, sticky="w", padx=(8, 0))

        row4_bottom = ttk.Frame(options_frame)
        row4_bottom.grid(row=1, column=0, sticky="ew", pady=(10, 0))
        for idx in range(12):
            row4_bottom.columnconfigure(idx, weight=1 if idx in {0, 3, 6, 8, 10, 11} else 0)

        self.generation_thinking_check = ttk.Checkbutton(
            row4_bottom,
            text="生成用思考",
            variable=self.generation_thinking_var,
        )
        self.generation_thinking_check.grid(row=0, column=0, sticky="w")
        self.generation_reasoning_effort_label = ttk.Label(row4_bottom, text="生成强度")
        self.generation_reasoning_effort_label.grid(row=0, column=1, sticky="w", padx=(8, 6))
        self.generation_reasoning_effort_combo = ttk.Combobox(
            row4_bottom,
            textvariable=self.generation_reasoning_effort_var,
            values=get_provider_reasoning_effort_options(self._effective_provider()),
            state="readonly",
            width=8,
        )
        self.generation_reasoning_effort_combo.grid(row=0, column=2, sticky="w", padx=(0, 18))
        self.review_thinking_check = ttk.Checkbutton(
            row4_bottom,
            text="审核用思考",
            variable=self.review_thinking_var,
        )
        self.review_thinking_check.grid(row=0, column=3, sticky="w")
        self.review_reasoning_effort_label = ttk.Label(row4_bottom, text="审核强度")
        self.review_reasoning_effort_label.grid(row=0, column=4, sticky="w", padx=(8, 6))
        self.review_reasoning_effort_combo = ttk.Combobox(
            row4_bottom,
            textvariable=self.review_reasoning_effort_var,
            values=get_provider_reasoning_effort_options(self._effective_provider()),
            state="readonly",
            width=8,
        )
        self.review_reasoning_effort_combo.grid(row=0, column=5, sticky="w", padx=(0, 18))
        ttk.Checkbutton(row4_bottom, text="Agent审核回修", variable=self.agent_review_var).grid(
            row=0, column=6, sticky="w", padx=(0, 18)
        )
        ttk.Label(row4_bottom, text="回修轮数").grid(row=0, column=7, sticky="w")
        ttk.Spinbox(
            row4_bottom,
            from_=1,
            to=5,
            increment=1,
            textvariable=self.review_rounds_var,
            width=6,
        ).grid(row=0, column=8, sticky="w", padx=(8, 18))
        ttk.Checkbutton(row4_bottom, text="覆盖旧结果", variable=self.overwrite_var).grid(
            row=0, column=9, sticky="w", padx=(0, 18)
        )
        ttk.Checkbutton(row4_bottom, text="分段稳定模式", variable=self.stable_segment_mode_var).grid(
            row=0, column=10, sticky="w", padx=(0, 18)
        )

        row5 = ttk.Frame(main)
        row5.grid(row=5, column=0, columnspan=3, sticky="ew", pady=(12, 0))
        row5.columnconfigure(6, weight=1)

        self.scan_button = ttk.Button(
            row5,
            text="扫描剧本",
            command=lambda: self.scan_episodes(force_directory_scan=True),
        )
        self.split_button = ttk.Button(row5, text="拆分合集", command=self.split_collection)
        self.split_button.grid(row=0, column=0, padx=(0, 8))
        self.scan_button.grid(row=0, column=1, padx=(0, 8))
        self.start_button = ttk.Button(row5, text="开始生成", command=self.start_generation)
        self.start_button.grid(row=0, column=2, padx=(0, 8))
        self.remove_button = ttk.Button(row5, text="移除选中", command=self.remove_selected_inputs)
        self.remove_button.grid(row=0, column=3, padx=(0, 8))
        ttk.Button(row5, text="保存设置", command=self.save_settings).grid(row=0, column=4, padx=(0, 8))
        ttk.Button(row5, text="打开输出目录", command=self.open_output_dir).grid(row=0, column=5, padx=(0, 12))
        ttk.Label(row5, textvariable=self.status_var).grid(row=0, column=6, sticky="w")

        ttk.Progressbar(main, variable=self.progress_var, maximum=100).grid(
            row=6, column=0, columnspan=3, sticky="ew", pady=(8, 10)
        )
        ttk.Label(
            main,
            text="可直接拖入：文件夹 / 提示词 .txt / 剧本 .docx。开启 Agent 审核时会自动按单集请求执行，用并发提速。",
        ).grid(row=7, column=0, columnspan=3, sticky="w", pady=(0, 8))

        self.tree = ttk.Treeview(
            main,
            columns=("episode", "source", "chars", "output"),
            show="headings",
            height=14,
            selectmode="extended",
        )
        self.tree.grid(row=8, column=0, columnspan=3, sticky="nsew")
        self.tree.bind("<Delete>", self.remove_selected_inputs)
        main.rowconfigure(8, weight=1)
        for key, title, width in (
            ("episode", "集数", 70),
            ("source", "源文件", 380),
            ("chars", "字符数", 90),
            ("output", "输出文件", 260),
        ):
            self.tree.heading(key, text=title)
            self.tree.column(key, width=width, anchor="w")

        log_frame = ttk.Frame(main)
        log_frame.grid(row=9, column=0, columnspan=3, sticky="nsew", pady=(12, 0))
        main.rowconfigure(9, weight=1)
        log_frame.rowconfigure(0, weight=1)
        log_frame.columnconfigure(0, weight=1)

        self.log_text = tk.Text(log_frame, height=14, wrap="none")
        self.log_text.grid(row=0, column=0, sticky="nsew")
        self.log_text.configure(state="disabled")
        scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=self.log_text.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.log_text.configure(yscrollcommand=scrollbar.set)
        self._sync_episode_action_states()

    def _init_drag_drop(self) -> None:
        if windnd is None:
            self._log("[warn] 未安装 windnd，拖拽功能不可用。")
            append_app_log("drag-drop disabled: windnd import failed")
            return
        windnd.hook_dropfiles(self.root, func=self._on_dropfiles, force_unicode=True)
        append_app_log("drag-drop initialized with windnd")

    def _teardown_drag_drop(self) -> None:
        return None

    def _on_dropfiles(self, dropped_items) -> None:
        try:
            normalized_items = self._normalize_drop_items(dropped_items)
            append_app_log(f"drop callback received {len(normalized_items)} item(s): {normalized_items!r}")
            self.log_queue.put(("drop", normalized_items))
        except Exception as exc:
            append_app_log(f"drop callback crashed: {exc!r}; raw={dropped_items!r}")
            self.log_queue.put(("drop_error", str(exc)))

    def _handle_drop_callback_error(self, error_message: str) -> None:
        self._log(f"[error] 拖拽回调异常：{error_message}")
        self.status_var.set("状态：拖拽失败")
        messagebox.showerror("拖拽失败", f"{error_message}\n\n详细日志：{APP_LOG_PATH}")

    def _report_callback_exception(self, exc_type, exc_value, exc_traceback) -> None:
        details = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        append_app_log("tk callback exception:\n" + details.rstrip())
        self._log(f"[error] GUI 回调异常：{exc_value}")
        self.status_var.set("状态：程序异常")
        messagebox.showerror("程序异常", f"{exc_value}\n\n详细日志：{APP_LOG_PATH}")

    def _normalize_drop_items(self, dropped_items) -> list[str]:
        if dropped_items is None:
            return []
        if isinstance(dropped_items, (str, bytes, bytearray, os.PathLike)):
            raw_items = [dropped_items]
        else:
            raw_items = list(dropped_items)

        normalized: list[str] = []
        for item in raw_items:
            normalized.extend(self._expand_drop_item(item))
        return [item for item in normalized if item.strip()]

    def _expand_drop_item(self, item) -> list[str]:
        if isinstance(item, os.PathLike):
            value = os.fspath(item)
        elif isinstance(item, bytes):
            try:
                value = item.decode("utf-8")
            except UnicodeDecodeError:
                value = item.decode("gbk", errors="replace")
        elif isinstance(item, bytearray):
            try:
                value = bytes(item).decode("utf-8")
            except UnicodeDecodeError:
                value = bytes(item).decode("gbk", errors="replace")
        else:
            value = str(item)

        value = value.strip()
        if not value:
            return []

        if "{" not in value and "}" not in value:
            return [value.strip('"')]

        if value.startswith("{") and value.endswith("}") and "} {" not in value and "},{" not in value:
            return [value[1:-1].strip().strip('"')]

        try:
            split_values = list(self.root.tk.splitlist(value))
        except Exception:
            split_values = [value]

        expanded: list[str] = []
        for entry in split_values:
            cleaned = str(entry).strip().strip('"')
            if cleaned:
                expanded.append(cleaned)
        return expanded

    def _provider_key_label(self, provider: str) -> str:
        return get_provider_api_key_label(provider)

    def _effective_provider(self) -> str:
        provider = self.provider_var.get().strip() or DEFAULT_PROVIDER
        if provider not in PROVIDER_CONFIGS:
            return DEFAULT_PROVIDER
        return provider

    def _effective_model(self, provider: str | None = None) -> str:
        resolved_provider = provider or self._effective_provider()
        return self.model_var.get().strip() or resolve_model(resolved_provider)

    def _effective_generation_reasoning_effort(self, provider: str | None = None) -> str:
        resolved_provider = provider or self._effective_provider()
        return (
            normalize_reasoning_effort(resolved_provider, self.generation_reasoning_effort_var.get().strip())
            or DEFAULT_GENERATION_REASONING_EFFORT
        )

    def _effective_review_reasoning_effort(self, provider: str | None = None) -> str:
        resolved_provider = provider or self._effective_provider()
        return (
            normalize_reasoning_effort(resolved_provider, self.review_reasoning_effort_var.get().strip())
            or DEFAULT_REVIEW_REASONING_EFFORT
        )

    def _recommended_max_tokens(self, provider: str | None = None, model: str | None = None) -> int:
        resolved_provider = provider or self._effective_provider()
        resolved_model = model or self._effective_model(resolved_provider)
        return resolve_default_max_tokens_for_model(resolved_provider, resolved_model)

    def _output_path_for_episode(self, out_dir: Path, episode, index: int) -> Path:
        return make_output_path(out_dir, episode, index, model=self._effective_model())

    def _sync_recommended_max_tokens(self, *, force: bool) -> None:
        recommended = self._recommended_max_tokens()
        current = int(self.max_tokens_var.get())
        legacy_deepseek_default = (
            self._effective_provider() == PROVIDER_DEEPSEEK
            and current == 12000
            and self._effective_model().strip().lower()
            in {"deepseek-v4-flash", "deepseek-v4-pro", "deepseek-chat", "deepseek-reasoner"}
        )
        if force or current <= 0 or current == self._last_recommended_max_tokens or legacy_deepseek_default:
            self.max_tokens_var.set(recommended)
        self._last_recommended_max_tokens = recommended

    def _sync_provider_ui(self) -> None:
        if hasattr(self, "api_key_label"):
            provider = self._effective_provider()
            self.api_key_label.configure(text=self._provider_key_label(provider))
            if hasattr(self, "model_combo"):
                self.model_combo.configure(values=get_provider_model_options(provider))
            if hasattr(self, "generation_thinking_check") and hasattr(self, "review_thinking_check"):
                supports_thinking = provider_supports_thinking(provider)
                supports_reasoning_effort = provider_supports_reasoning_effort(provider)
                if supports_thinking:
                    self.generation_thinking_check.configure(text="生成用思考", state="normal")
                    self.review_thinking_check.configure(text="审核用思考", state="normal")
                else:
                    self.generation_thinking_var.set(False)
                    self.review_thinking_var.set(False)
                    self.generation_thinking_check.configure(
                        text="生成用思考（当前供应商不支持）",
                        state="disabled",
                    )
                    self.review_thinking_check.configure(
                        text="审核用思考（当前供应商不支持）",
                        state="disabled",
                    )
                if hasattr(self, "generation_reasoning_effort_combo") and hasattr(self, "review_reasoning_effort_combo"):
                    effort_options = get_provider_reasoning_effort_options(provider)
                    self.generation_reasoning_effort_var.set(self._effective_generation_reasoning_effort(provider))
                    self.review_reasoning_effort_var.set(self._effective_review_reasoning_effort(provider))
                    self.generation_reasoning_effort_combo.configure(values=effort_options)
                    self.review_reasoning_effort_combo.configure(values=effort_options)
                    if supports_reasoning_effort and self.generation_thinking_var.get():
                        self.generation_reasoning_effort_label.configure(text="生成强度")
                        self.generation_reasoning_effort_combo.configure(state="readonly")
                    else:
                        disabled_text = "生成强度" if supports_reasoning_effort else "生成强度（当前供应商不支持）"
                        self.generation_reasoning_effort_label.configure(text=disabled_text)
                        self.generation_reasoning_effort_combo.configure(state="disabled")
                    if supports_reasoning_effort and self.review_thinking_var.get():
                        self.review_reasoning_effort_label.configure(text="审核强度")
                        self.review_reasoning_effort_combo.configure(state="readonly")
                    else:
                        disabled_text = "审核强度" if supports_reasoning_effort else "审核强度（当前供应商不支持）"
                        self.review_reasoning_effort_label.configure(text=disabled_text)
                        self.review_reasoning_effort_combo.configure(state="disabled")

    def _on_thinking_changed(self, *_args) -> None:
        self._sync_provider_ui()

    def _apply_provider_defaults(self, provider: str, *, force: bool) -> None:
        default_model = resolve_model(provider)
        default_api_base = resolve_api_base(provider)
        if force or not self.model_var.get().strip():
            self.model_var.set(default_model)
        if force or not self.api_base_var.get().strip():
            self.api_base_var.set(default_api_base)
        self._sync_recommended_max_tokens(force=force)
        self._sync_provider_ui()
        self._refresh_episode_table()

    def _on_provider_changed(self, _event=None) -> None:
        provider = self._effective_provider()
        self.provider_var.set(provider)
        self._apply_provider_defaults(provider, force=True)

    def _on_model_name_changed(self, *_args) -> None:
        self._sync_recommended_max_tokens(force=False)
        self._refresh_episode_table()

    def _refresh_episode_table(self) -> None:
        if not hasattr(self, "tree"):
            return
        self.tree.delete(*self.tree.get_children())
        self.tree_row_paths = {}
        if not self.episodes:
            self._sync_episode_action_states()
            return

        project_text = self.project_var.get().strip()
        default_output_dir = (Path(project_text) if project_text else Path.cwd()) / DEFAULT_OUTPUT_DIR
        output_dir = Path(self.output_var.get().strip() or default_output_dir)

        for index, episode in enumerate(self.episodes, start=1):
            output_name = self._output_path_for_episode(output_dir, episode, index).name
            episode_number = episode.episode_number
            episode_label = str(episode_number) if episode_number is not None else "-"
            item_id = self.tree.insert(
                "",
                "end",
                values=(episode_label, episode.source_path.name, len(episode.script_text), output_name),
            )
            self.tree_row_paths[item_id] = episode.source_path
        self._sync_episode_action_states()

    def _sync_episode_action_states(self) -> None:
        if hasattr(self, "remove_button"):
            is_running = self.worker_thread is not None and self.worker_thread.is_alive()
            state = "normal" if self.episodes and not is_running else "disabled"
            self.remove_button.configure(state=state)

    def remove_selected_inputs(self, _event=None):
        if self.worker_thread and self.worker_thread.is_alive():
            self.status_var.set("状态：生成进行中，暂时不能移除文件")
            return "break"

        selected_items = self.tree.selection()
        if not selected_items:
            self.status_var.set("状态：请先在列表中选择要移除的文件")
            return "break"

        selected_paths = {
            self.tree_row_paths[item_id]
            for item_id in selected_items
            if item_id in self.tree_row_paths
        }
        if not selected_paths:
            self.status_var.set("状态：未找到可移除的文件")
            return "break"

        remaining_episodes = [episode for episode in self.episodes if episode.source_path not in selected_paths]
        removed_count = len(self.episodes) - len(remaining_episodes)
        if removed_count <= 0:
            self.status_var.set("状态：未移除任何文件")
            return "break"

        self.episodes = remaining_episodes
        self.selected_script_paths = [episode.source_path for episode in remaining_episodes]
        removed_names = sorted((path.name for path in selected_paths), key=str.lower)
        removed_preview = "、".join(removed_names[:3])
        self._refresh_episode_table()
        self.progress_var.set(0)

        if self.episodes:
            self.status_var.set(f"状态：已移除 {removed_count} 个文件，剩余 {len(self.episodes)} 集")
        else:
            self.status_var.set("状态：当前任务已清空，点击“扫描剧本”可重新按目录扫描")

        self._log(f"[info] 已从当前任务移除 {removed_count} 个文件（未删除磁盘文件）。")
        if removed_preview:
            suffix = "..." if len(removed_names) > 3 else ""
            self._log(f"[info] Removed: {removed_preview}{suffix}")
        return "break"

    def _handle_dropped_paths(self, dropped_items: list[str]) -> None:
        try:
            append_app_log(f"drop handling started: {dropped_items!r}")
            dropped_paths = [Path(item) for item in dropped_items]
            existing_paths = [path for path in normalize_paths(dropped_paths) if path.exists()]
            if not existing_paths:
                raise ValueError("拖入的路径不存在或无法识别。")

            directories = [path for path in existing_paths if path.is_dir()]
            files = [path for path in existing_paths if path.is_file()]
            prompt_file = pick_prompt_file(files)
            script_files = [
                path
                for path in files
                if (
                    path.suffix.lower() == ".docx"
                    or (path.suffix.lower() == ".txt" and not is_prompt_like_file(path))
                )
                and not path.name.startswith("~$")
            ]
            unsupported_files = [
                path.name
                for path in files
                if path not in script_files and path != prompt_file
            ]

            project_candidates = directories[:]
            if script_files:
                project_candidates.append(common_parent(script_files) or script_files[0].parent)
            elif prompt_file is not None:
                project_candidates.append(prompt_file.parent)
            project_dir = common_parent(project_candidates) if project_candidates else None

            should_scan = bool(directories or script_files)

            if project_dir is not None:
                self.project_var.set(str(project_dir))
                if not self.output_var.get().strip():
                    self.output_var.set(str(project_dir / DEFAULT_OUTPUT_DIR))

            if prompt_file is not None:
                self.prompt_var.set(str(prompt_file))
            elif project_dir is not None and not Path(self.prompt_var.get().strip()).is_file():
                try:
                    self.prompt_var.set(str(find_prompt_file(project_dir, None)))
                except Exception:
                    pass

            self.selected_script_paths = script_files or None

            dropped_labels: list[str] = []
            if directories:
                dropped_labels.append(f"{len(directories)} 个文件夹")
            if prompt_file is not None:
                dropped_labels.append(f"提示词 {prompt_file.name}")
            if script_files:
                dropped_labels.append(f"{len(script_files)} 个剧本")

            if project_dir is not None and should_scan:
                self._log(f"[info] 已拖入：{', '.join(dropped_labels) or project_dir}")
                self.status_var.set("状态：已接收拖拽内容，正在扫描")
                self.scan_episodes()
            elif prompt_file is not None:
                self._log(f"[info] 已拖入提示词：{prompt_file.name}")
                self.status_var.set("状态：提示词已更新")
            elif unsupported_files:
                unsupported_list = "、".join(unsupported_files)
                raise ValueError(
                    "仅支持拖入文件夹、提示词 .txt、单集剧本 .docx/.txt。\n"
                    f"当前不支持：{unsupported_list}"
                )
            else:
                raise ValueError("请拖入文件夹、提示词 .txt 或剧本 .docx。")
        except Exception as exc:
            append_app_log(f"drop handling failed: {exc!r}; items={dropped_items!r}")
            self._log(f"[error] 拖拽失败：{exc}")
            messagebox.showerror("拖拽失败", f"{exc}\n\n详细日志：{APP_LOG_PATH}")

    def _labeled_entry(self, parent, label: str, row: int, variable: StringVar, browse_command) -> None:
        ttk.Label(parent, text=label).grid(row=row, column=0, sticky="w", pady=(0, 8))
        ttk.Entry(parent, textvariable=variable).grid(row=row, column=1, sticky="ew", padx=(10, 12), pady=(0, 8))
        ttk.Button(parent, text="浏览", command=browse_command).grid(row=row, column=2, sticky="e", pady=(0, 8))

    def _choose_project(self) -> None:
        selected = filedialog.askdirectory(initialdir=self.project_var.get() or str(Path.cwd()))
        if selected:
            self.selected_script_paths = None
            self.project_var.set(selected)
            if not self.output_var.get():
                self.output_var.set(str(Path(selected) / DEFAULT_OUTPUT_DIR))

    def _choose_prompt(self) -> None:
        selected = filedialog.askopenfilename(
            initialdir=self.project_var.get() or str(Path.cwd()),
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )
        if selected:
            self.prompt_var.set(selected)

    def _choose_output(self) -> None:
        selected = filedialog.askdirectory(initialdir=self.output_var.get() or self.project_var.get() or str(Path.cwd()))
        if selected:
            self.output_var.set(selected)

    def split_collection(self) -> None:
        try:
            selected = filedialog.askopenfilename(
                initialdir=self.project_var.get() or str(Path.cwd()),
                filetypes=[
                    ("Collection scripts", "*.docx *.txt"),
                    ("Word documents", "*.docx"),
                    ("Text files", "*.txt"),
                    ("All files", "*.*"),
                ],
            )
            if not selected:
                return

            source_path = Path(selected)
            if not source_path.is_file():
                raise ValueError("请选择有效的合集文件。")

            project_path = source_path.parent
            split_dir = project_path / DEFAULT_SPLIT_DIR_NAME / sanitize_filename_part(source_path.stem)
            episode_paths = split_episode_collection_file(source_path, split_dir, overwrite=True)
            if not episode_paths:
                raise ValueError("拆分失败：没有生成任何分集文件。")

            self.project_var.set(str(project_path))
            if not self.output_var.get().strip():
                self.output_var.set(str(project_path / DEFAULT_OUTPUT_DIR))
            if not self.prompt_var.get().strip():
                try:
                    self.prompt_var.set(str(find_prompt_file(project_path, None)))
                except Exception:
                    pass

            self.selected_script_paths = episode_paths
            self._log(
                f"[info] 已拆分合集：{source_path.name} -> {len(episode_paths)} 集，目录：{split_dir}"
            )
            self.status_var.set(f"状态：合集已拆分，共 {len(episode_paths)} 集")
            self.scan_episodes()
        except Exception as exc:
            self._log(f"[error] 拆分失败：{exc}")
            messagebox.showerror("拆分失败", str(exc))

    def _load_settings(self) -> None:
        default_project = str(Path(__file__).resolve().parent)
        self.project_var.set(default_project)
        self.output_var.set(str(Path(default_project) / DEFAULT_OUTPUT_DIR))
        self.provider_var.set(DEFAULT_PROVIDER)
        self._apply_provider_defaults(DEFAULT_PROVIDER, force=True)

        if not SETTINGS_PATH.exists():
            try:
                self.prompt_var.set(str(find_prompt_file(Path(default_project), None)))
            except Exception:
                pass
            self._sync_provider_ui()
            return

        try:
            data = json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
        except Exception:
            return

        provider = data.get("provider", DEFAULT_PROVIDER)
        if provider not in PROVIDER_CONFIGS:
            provider = DEFAULT_PROVIDER
        self.project_var.set(data.get("project_folder", default_project))
        self.prompt_var.set(data.get("prompt_path", ""))
        self.output_var.set(data.get("out_dir", str(Path(default_project) / DEFAULT_OUTPUT_DIR)))
        self.provider_var.set(provider)
        self.model_var.set(data.get("model", resolve_model(provider)))
        self.api_base_var.set(data.get("api_base", resolve_api_base(provider)))
        legacy_thinking = bool(data.get("thinking_enabled", True))
        self.generation_thinking_var.set(bool(data.get("generation_thinking_enabled", legacy_thinking)))
        self.review_thinking_var.set(bool(data.get("review_thinking_enabled", DEFAULT_REVIEW_THINKING_ENABLED)))
        self.generation_reasoning_effort_var.set(
            normalize_reasoning_effort(
                provider,
                data.get("generation_reasoning_effort", DEFAULT_GENERATION_REASONING_EFFORT),
            )
            or DEFAULT_GENERATION_REASONING_EFFORT
        )
        self.review_reasoning_effort_var.set(
            normalize_reasoning_effort(
                provider,
                data.get("review_reasoning_effort", DEFAULT_REVIEW_REASONING_EFFORT),
            )
            or DEFAULT_REVIEW_REASONING_EFFORT
        )
        self.overwrite_var.set(bool(data.get("overwrite", False)))
        self.agent_review_var.set(bool(data.get("agent_review_enabled", DEFAULT_AGENT_REVIEW_ENABLED)))
        self.stable_segment_mode_var.set(bool(data.get("stable_segment_mode", True)))
        self.temperature_var.set(float(data.get("temperature", DEFAULT_TEMPERATURE)))
        self.timeout_var.set(int(data.get("timeout_seconds", DEFAULT_TIMEOUT_SECONDS)))
        recommended_max_tokens = resolve_default_max_tokens_for_model(provider, self.model_var.get().strip())
        saved_max_tokens = data.get("max_tokens")
        if (
            saved_max_tokens is None
            or (
                provider == PROVIDER_DEEPSEEK
                and self.model_var.get().strip().lower() == "deepseek-chat"
                and int(saved_max_tokens) == 12000
            )
        ):
            self.max_tokens_var.set(recommended_max_tokens)
        else:
            self.max_tokens_var.set(int(saved_max_tokens))
        self.delay_var.set(float(data.get("delay_seconds", DEFAULT_DELAY_SECONDS)))
        self.max_retries_var.set(int(data.get("max_retries", DEFAULT_MAX_RETRIES)))
        self.parallelism_var.set(int(data.get("parallelism", DEFAULT_PARALLELISM)))
        self.episodes_per_request_var.set(int(data.get("episodes_per_request", DEFAULT_EPISODES_PER_REQUEST)))
        self.review_rounds_var.set(int(data.get("review_rounds", DEFAULT_AGENT_REVIEW_ROUNDS)))
        self._last_recommended_max_tokens = recommended_max_tokens
        self._sync_provider_ui()

        encrypted_key = data.get("api_key_protected", "")
        if encrypted_key:
            try:
                self.api_key_var.set(unprotect_secret(encrypted_key))
            except Exception:
                self.api_key_var.set("")

    def save_settings(self) -> None:
        data = {
            "project_folder": self.project_var.get().strip(),
            "prompt_path": self.prompt_var.get().strip(),
            "out_dir": self.output_var.get().strip(),
            "provider": self.provider_var.get().strip(),
            "model": self.model_var.get().strip(),
            "api_base": self.api_base_var.get().strip(),
            "generation_thinking_enabled": bool(self.generation_thinking_var.get()),
            "review_thinking_enabled": bool(self.review_thinking_var.get()),
            "generation_reasoning_effort": self.generation_reasoning_effort_var.get().strip() or DEFAULT_GENERATION_REASONING_EFFORT,
            "review_reasoning_effort": self.review_reasoning_effort_var.get().strip() or DEFAULT_REVIEW_REASONING_EFFORT,
            "overwrite": bool(self.overwrite_var.get()),
            "agent_review_enabled": bool(self.agent_review_var.get()),
            "stable_segment_mode": bool(self.stable_segment_mode_var.get()),
            "temperature": float(self.temperature_var.get()),
            "timeout_seconds": int(self.timeout_var.get()),
            "max_tokens": int(self.max_tokens_var.get()),
            "delay_seconds": float(self.delay_var.get()),
            "max_retries": int(self.max_retries_var.get()),
            "parallelism": int(self.parallelism_var.get()),
            "episodes_per_request": int(self.episodes_per_request_var.get()),
            "review_rounds": int(self.review_rounds_var.get()),
            "api_key_protected": protect_secret(self.api_key_var.get().strip()),
        }
        SETTINGS_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        self._log("设置已保存。API Key 已按当前 Windows 用户加密保存。")
        self.status_var.set("状态：设置已保存")
        messagebox.showinfo("保存成功", "设置已保存。")

    def _append_line_to_path(self, path: Path, message: str) -> None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(f"[{timestamp}] {message}\n")

    def _create_run_log_path(self, out_dir: Path) -> Path:
        logs_dir = out_dir / RUN_LOGS_DIRNAME
        logs_dir.mkdir(parents=True, exist_ok=True)
        base_name = f"storyboard-run-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
        candidate = logs_dir / f"{base_name}.log"
        suffix = 1
        while candidate.exists():
            candidate = logs_dir / f"{base_name}-{suffix}.log"
            suffix += 1
        return candidate

    def _describe_run_log_path(self) -> str:
        if self.active_run_log_path is not None:
            return str(self.active_run_log_path)
        if self.last_run_log_path is not None:
            return str(self.last_run_log_path)
        return str(APP_LOG_PATH)

    def _summarize_failure(self, payload: object) -> str:
        lines = [line.strip() for line in str(payload).splitlines() if line.strip()]
        if not lines:
            return "执行失败。"
        head = lines[0]
        if head.startswith("Some episodes failed:"):
            for line in lines[1:]:
                if line.startswith("["):
                    continue
                return line
        return head

    def _log(self, message: str) -> None:
        self.log_text.configure(state="normal")
        self.log_text.insert("end", message + "\n")
        self.log_text.see("end")
        self.log_text.configure(state="disabled")
        if self.active_run_log_path is not None:
            try:
                self._append_line_to_path(self.active_run_log_path, message)
            except Exception as exc:
                append_app_log(f"run log write failed: {exc!r}")

    def _load_episode_inputs(self, project_path: Path, *, force_directory_scan: bool = False) -> list:
        if force_directory_scan:
            self.selected_script_paths = None
        if self.selected_script_paths is not None:
            existing_script_paths = [path for path in self.selected_script_paths if path.exists()]
            self.selected_script_paths = existing_script_paths
            if existing_script_paths:
                return build_episode_inputs_from_paths(existing_script_paths)
            return []
        return build_episode_inputs(project_path, "*.docx")

    def scan_episodes(self, force_directory_scan: bool = False) -> None:
        try:
            project_path = Path(self.project_var.get().strip())
            if not project_path.is_dir():
                raise ValueError("请先选择有效的项目目录。")
            prompt_path = find_prompt_file(project_path, Path(self.prompt_var.get().strip()) if self.prompt_var.get().strip() else None)
            self.prompt_var.set(str(prompt_path))
            episodes = self._load_episode_inputs(project_path, force_directory_scan=force_directory_scan)
            if not episodes:
                raise ValueError("没有找到可处理的剧本文件。")

            self.episodes = []
            output_dir = Path(self.output_var.get().strip() or project_path / DEFAULT_OUTPUT_DIR)
            self.output_var.set(str(output_dir))
            self.episodes = list(episodes)
            self._refresh_episode_table()

            self.status_var.set(f"状态：已扫描到 {len(episodes)} 集剧本")
            self.progress_var.set(0)
            self._log(f"[info] Prompt: {Path(self.prompt_var.get()).name}")
            self._log(f"[info] Episodes found: {len(episodes)}")
        except Exception as exc:
            self._log(f"[error] 扫描失败：{exc}")
            messagebox.showerror("扫描失败", str(exc))

    def open_output_dir(self) -> None:
        target = self.output_var.get().strip()
        if not target:
            return
        Path(target).mkdir(parents=True, exist_ok=True)
        os.startfile(target)

    def start_generation(self) -> None:
        if self.worker_thread and self.worker_thread.is_alive():
            return
        if not self.episodes:
            self.scan_episodes()
            if not self.episodes:
                return

        api_key = self.api_key_var.get().strip()
        if not api_key:
            messagebox.showerror("启动失败", "请填写当前供应商的 API Key。")
            return
        if int(self.parallelism_var.get()) < 1:
            messagebox.showerror("启动失败", "并发数至少要为 1。")
            return
        episodes_per_request = int(self.episodes_per_request_var.get())
        if episodes_per_request < 1 or episodes_per_request > MAX_EPISODES_PER_REQUEST:
            messagebox.showerror(
                "启动失败",
                f"单次处理集数必须在 1 到 {MAX_EPISODES_PER_REQUEST} 之间。",
            )
            return
        if bool(self.agent_review_var.get()) and int(self.review_rounds_var.get()) < 1:
            messagebox.showerror("启动失败", "开启 Agent 审核回修时，回修轮数至少要为 1。")
            return

        out_dir = Path(self.output_var.get().strip())
        out_dir.mkdir(parents=True, exist_ok=True)

        if not self.overwrite_var.get():
            existing = []
            for index, episode in enumerate(self.episodes, start=1):
                output_path = self._output_path_for_episode(out_dir, episode, index)
                if output_path.exists():
                    existing.append(output_path.name)
            if existing and len(existing) == len(self.episodes):
                message = "检测到所有输出文件都已存在：\n\n" + "\n".join(existing) + "\n\n如果要重新生成，请先勾选 [覆盖旧结果]。"
                self.status_var.set("状态：全部结果已存在")
                self._log("[info] 所有输出文件都已存在，当前不会重新生成。")
                messagebox.showinfo("无需生成", message)
                return

        self.active_run_log_path = self._create_run_log_path(out_dir)
        self.last_run_log_path = self.active_run_log_path
        self._log(f"[info] Run log: {self.active_run_log_path}")
        self.save_settings_silent()
        self.split_button.configure(state="disabled")
        self.scan_button.configure(state="disabled")
        self.start_button.configure(state="disabled")
        self.remove_button.configure(state="disabled")
        self.progress_var.set(0)
        self.status_var.set("状态：正在生成...")

        self.worker_thread = threading.Thread(target=self._run_generation, daemon=True)
        self.worker_thread.start()

    def save_settings_silent(self) -> None:
        data = {
            "project_folder": self.project_var.get().strip(),
            "prompt_path": self.prompt_var.get().strip(),
            "out_dir": self.output_var.get().strip(),
            "provider": self.provider_var.get().strip(),
            "model": self.model_var.get().strip(),
            "api_base": self.api_base_var.get().strip(),
            "generation_thinking_enabled": bool(self.generation_thinking_var.get()),
            "review_thinking_enabled": bool(self.review_thinking_var.get()),
            "generation_reasoning_effort": self.generation_reasoning_effort_var.get().strip() or DEFAULT_GENERATION_REASONING_EFFORT,
            "review_reasoning_effort": self.review_reasoning_effort_var.get().strip() or DEFAULT_REVIEW_REASONING_EFFORT,
            "overwrite": bool(self.overwrite_var.get()),
            "agent_review_enabled": bool(self.agent_review_var.get()),
            "stable_segment_mode": bool(self.stable_segment_mode_var.get()),
            "temperature": float(self.temperature_var.get()),
            "timeout_seconds": int(self.timeout_var.get()),
            "max_tokens": int(self.max_tokens_var.get()),
            "delay_seconds": float(self.delay_var.get()),
            "max_retries": int(self.max_retries_var.get()),
            "parallelism": int(self.parallelism_var.get()),
            "episodes_per_request": int(self.episodes_per_request_var.get()),
            "review_rounds": int(self.review_rounds_var.get()),
            "api_key_protected": protect_secret(self.api_key_var.get().strip()),
        }
        SETTINGS_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def _queue_progress(self, completed: int, total: int) -> None:
        percent = 100 if total <= 0 else int(completed / total * 100)
        self.log_queue.put(("progress", percent))

    def _run_generation(self) -> None:
        try:
            project_path = Path(self.project_var.get().strip())
            prompt_path = find_prompt_file(project_path, Path(self.prompt_var.get().strip()) if self.prompt_var.get().strip() else None)
            prompt_text = read_utf8_text(prompt_path)
            out_dir = Path(self.output_var.get().strip())
            api_key = self.api_key_var.get().strip()
            provider = self._effective_provider()
            model = self._effective_model(provider)
            api_base = self.api_base_var.get().strip() or resolve_api_base(provider)
            validate_api_key_for_provider(provider, api_key)
            temperature = float(self.temperature_var.get())
            timeout_seconds = int(self.timeout_var.get())
            max_tokens = int(self.max_tokens_var.get())
            if max_tokens <= 0:
                max_tokens = self._recommended_max_tokens(provider, model)
            delay_seconds = float(self.delay_var.get())
            max_retries = int(self.max_retries_var.get())
            parallelism = int(self.parallelism_var.get())
            episodes_per_request = int(self.episodes_per_request_var.get())
            review_rounds = int(self.review_rounds_var.get())
            overwrite = bool(self.overwrite_var.get())
            generation_thinking_enabled = bool(self.generation_thinking_var.get())
            review_thinking_enabled = bool(self.review_thinking_var.get())
            generation_reasoning_effort = self._effective_generation_reasoning_effort(provider)
            review_reasoning_effort = self._effective_review_reasoning_effort(provider)
            agent_review_enabled = bool(self.agent_review_var.get())
            stable_segment_mode = bool(self.stable_segment_mode_var.get())
            review_skill_text = load_review_skill_text()

            log_generation_plan(
                prompt_path=prompt_path,
                episodes=self.episodes,
                out_dir=out_dir,
                provider=provider,
                model=model,
                api_base=api_base,
                generation_thinking_enabled=generation_thinking_enabled,
                review_thinking_enabled=review_thinking_enabled,
                generation_reasoning_effort=generation_reasoning_effort,
                review_reasoning_effort=review_reasoning_effort,
                timeout_seconds=timeout_seconds,
                parallelism=parallelism,
                max_tokens=max_tokens,
                episodes_per_request=episodes_per_request,
                agent_review_enabled=agent_review_enabled,
                stable_segment_mode=stable_segment_mode,
                review_rounds=review_rounds,
                log=lambda message: self.log_queue.put(("log", message)),
            )
            run_batch_generation(
                episodes=self.episodes,
                prompt_text=prompt_text,
                out_dir=out_dir,
                provider=provider,
                api_base=api_base,
                api_key=api_key,
                model=model,
                generation_thinking_enabled=generation_thinking_enabled,
                review_thinking_enabled=review_thinking_enabled,
                generation_reasoning_effort=generation_reasoning_effort,
                review_reasoning_effort=review_reasoning_effort,
                temperature=temperature,
                timeout_seconds=timeout_seconds,
                max_tokens=max_tokens,
                max_retries=max_retries,
                delay_seconds=delay_seconds,
                overwrite=overwrite,
                parallelism=parallelism,
                episodes_per_request=episodes_per_request,
                agent_review_enabled=agent_review_enabled,
                stable_segment_mode=stable_segment_mode,
                review_rounds=review_rounds,
                review_skill_text=review_skill_text,
                log=lambda message: self.log_queue.put(("log", message)),
                on_progress=self._queue_progress,
            )

            self.log_queue.put(("done", None))
        except Exception as exc:
            self.log_queue.put(("error", str(exc)))

    def _drain_queue(self) -> None:
        try:
            while True:
                kind, payload = self.log_queue.get_nowait()
                if kind == "log":
                    self._log(str(payload))
                elif kind == "drop":
                    self._handle_dropped_paths(list(payload))
                elif kind == "drop_error":
                    self._handle_drop_callback_error(str(payload))
                elif kind == "progress":
                    self.progress_var.set(int(payload))
                    self.status_var.set(f"状态：已完成 {payload}%")
                elif kind == "done":
                    self.progress_var.set(100)
                    self.status_var.set("状态：生成完成")
                    self._log("[done] Batch generation finished.")
                    self.split_button.configure(state="normal")
                    self.scan_button.configure(state="normal")
                    self.start_button.configure(state="normal")
                    self._sync_episode_action_states()
                    log_path = self._describe_run_log_path()
                    messagebox.showinfo("完成", f"分镜生成完成。\n\n运行日志：{log_path}")
                    self.active_run_log_path = None
                elif kind == "error":
                    self.status_var.set("状态：执行失败")
                    self._log(f"[error] {payload}")
                    self.split_button.configure(state="normal")
                    self.scan_button.configure(state="normal")
                    self.start_button.configure(state="normal")
                    self._sync_episode_action_states()
                    log_path = self._describe_run_log_path()
                    summary = self._summarize_failure(payload)
                    messagebox.showerror(
                        "失败",
                        f"{summary}\n\n完整日志：{log_path}",
                    )
                    self.active_run_log_path = None
        except queue.Empty:
            pass
        self.root.after(150, self._drain_queue)

    def _on_close(self) -> None:
        try:
            self.save_settings_silent()
        except Exception:
            pass
        try:
            self._teardown_drag_drop()
        except Exception:
            pass
        self.root.destroy()


def main() -> int:
    root = Tk()
    app = StoryboardApp(root)
    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
