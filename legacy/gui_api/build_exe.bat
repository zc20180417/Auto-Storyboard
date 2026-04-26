@echo off
setlocal
set "PY=C:\Users\A\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
set "ROOT=%~dp0"
if "%ROOT:~-1%"=="\" set "ROOT=%ROOT:~0,-1%"
"%PY%" -c "import windnd" >nul 2>nul
if errorlevel 1 "%PY%" -m pip install windnd
"%PY%" -c "import PyInstaller" >nul 2>nul
if errorlevel 1 "%PY%" -m pip install pyinstaller
"%PY%" -m PyInstaller ^
  --noconfirm ^
  --clean ^
  --onefile ^
  --windowed ^
  --name AutoStoryboardGenerator ^
  --distpath "%ROOT%" ^
  --workpath "%ROOT%\build_pyinstaller" ^
  --specpath "%ROOT%" ^
  "%ROOT%\storyboard_gui_app.py"
