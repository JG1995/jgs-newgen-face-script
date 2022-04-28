@echo on
:start
py Script_faces.py
timeout /t 600 > NUL
goto start