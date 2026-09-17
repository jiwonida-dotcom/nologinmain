@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"

echo ============================================
echo  nologinMain - git push
echo  repo: https://github.com/jiwonida-dotcom/nologinmain
echo ============================================
echo.

git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
  echo [ERROR] git repository not found in this folder.
  pause
  exit /b 1
)

git status -s
echo.

set "MSG=%~1"
if "%MSG%"=="" set /p MSG=commit message (Enter = "update"): 
if "%MSG%"=="" set "MSG=update"

git add -A
git diff --cached --quiet
if errorlevel 1 (
  git commit -m "%MSG%"
  if errorlevel 1 (
    echo [ERROR] commit failed.
    pause
    exit /b 1
  )
) else (
  echo [INFO] nothing to commit - pushing existing commits.
)

git push -u origin main
if errorlevel 1 (
  echo.
  echo [ERROR] push failed. Check GitHub login (Git Credential Manager) or network.
  pause
  exit /b 1
)

echo.
echo [OK] pushed. Pages: https://jiwonida-dotcom.github.io/nologinmain/?v=%RANDOM%
echo      (first time: Settings ^> Pages ^> main / (root) ^> Save)
pause
endlocal
