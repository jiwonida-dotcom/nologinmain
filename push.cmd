@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion
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

git add -A
git diff --cached --quiet
if errorlevel 1 goto :commit
echo [INFO] nothing to commit - pushing existing commits.
goto :push

:commit
echo [changed files]
git diff --cached --name-status
echo.

rem ---- commit message: argument > auto-generated ----
set "MSG=%~1"
if not "%MSG%"=="" goto :docommit

rem timestamp
for /f "usebackq delims=" %%t in (`powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm'"`) do set "STAMP=%%t"

rem counts by status (A/M/D/R)
set /a NA=0, NM=0, ND=0, NR=0, N=0
for /f "usebackq tokens=1" %%s in (`git diff --cached --name-status`) do (
  set "S=%%s"
  set "S=!S:~0,1!"
  if "!S!"=="A" set /a NA+=1
  if "!S!"=="M" set /a NM+=1
  if "!S!"=="D" set /a ND+=1
  if "!S!"=="R" set /a NR+=1
  set /a N+=1
)

rem summary of counts
set "SUM="
if !NA! gtr 0 set "SUM=!SUM!add !NA! "
if !NM! gtr 0 set "SUM=!SUM!mod !NM! "
if !ND! gtr 0 set "SUM=!SUM!del !ND! "
if !NR! gtr 0 set "SUM=!SUM!ren !NR! "

rem first 3 file names
set "FILES="
set /a K=0
for /f "usebackq delims=" %%f in (`git diff --cached --name-only`) do (
  if !K! lss 3 (
    if "!FILES!"=="" (set "FILES=%%f") else (set "FILES=!FILES!, %%f")
  )
  set /a K+=1
)
if !N! gtr 3 set /a REST=!N!-3
if defined REST set "FILES=!FILES! +!REST!"

rem tag by area
set "AREA=update"
git diff --cached --name-only | findstr /b /c:"index.html" >nul && set "AREA=report"
git diff --cached --name-only | findstr /b /c:"docs/" >nul && set "AREA=docs"
git diff --cached --name-only | findstr /b /c:"docs/" >nul && git diff --cached --name-only | findstr /b /c:"index.html" >nul && set "AREA=docs+report"
git diff --cached --name-only | findstr /b /c:"assets/" >nul && set "AREA=assets"

set "MSG=!AREA!: !STAMP! · !SUM!(!FILES!)"

:docommit
echo [commit] !MSG!
git commit -q -m "!MSG!"
if errorlevel 1 (
  echo [ERROR] commit failed.
  pause
  exit /b 1
)

:push
echo.
git push -u origin main
if errorlevel 1 (
  echo.
  echo [ERROR] push failed. Check GitHub login (Git Credential Manager) or network.
  pause
  exit /b 1
)

echo.
echo [OK] pushed.
git log -1 --oneline
echo Pages: https://jiwonida-dotcom.github.io/nologinmain/?v=%RANDOM%
echo (first time: Settings ^> Pages ^> main / (root) ^> Save)
pause
endlocal
