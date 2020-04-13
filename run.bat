@ECHO OFF
cls && echo Setting virtual environment... && virtualenv env && pause && cls && ./env/Scripts/activate && cls && pip install flask && pause && cls && python src/app.py
endlocal