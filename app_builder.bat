@echo off
REM ====== Clean previous builds ======
echo Cleaning old builds...
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
del main.spec 2>nul

REM ====== Build with PyInstaller ======
echo Building game executable...
pyinstaller --onefile --windowed main.py ^
  --add-data "graphics;graphics" ^
  --add-data "fonts;fonts" ^
  --add-data "game_data.db;."

REM ====== Build Complete ======
echo.
echo ===================================
echo Build Complete!
echo Your EXE is in the "dist" folder.
echo ===================================
pause