@echo off
FOR /L %%i IN (1,1,3) DO (
    echo Running carv.py - Iteration %%i
    python carv.py
)
pause
