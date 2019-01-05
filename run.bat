@echo off
title Run IMDb Sync
echo 1. Running from Office
echo 2. Running from Home
echo(
set /p home=Where are you running this sync from: 
if %home% == 1 goto office
if %home% == 2 goto home

:office
cls
python run.py office mssql %*
pause
exit

:home
cls
echo Okay, you running this sync from Home
echo(
echo 1. MSSQL
echo 2. PostgreSQL
echo(
set /p sql=Which db are you running this sync on: 
if %sql% == 1 goto mssql
if %sql% == 2 goto postgres

:mssql
cls
python run.py home mysql %*
pause
exit

:postgres
cls
python run.py home postgresql %*
pause
exit