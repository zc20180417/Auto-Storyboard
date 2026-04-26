@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
if exist "%SCRIPT_DIR%AutoStoryboardGenerator.exe" (
  start "" "%SCRIPT_DIR%AutoStoryboardGenerator.exe"
  exit /b 0
)
if exist "%SCRIPT_DIR%dist\AutoStoryboardGenerator.exe" (
  start "" "%SCRIPT_DIR%dist\AutoStoryboardGenerator.exe"
  exit /b 0
)
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT_DIR%StoryboardGeneratorGUI.ps1"
set "ERR=%ERRORLEVEL%"
if not "%ERR%"=="0" (
  echo.
  echo Launch failed. Exit code: %ERR%
  echo.
  pause
)
