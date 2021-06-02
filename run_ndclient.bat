@ECHO OFF
REM Quick utility to run NoDetails Client without installing

SETLOCAL
SET PYTHONPATH=%~dp0\..\nodetails\code
SET TF_CPP_MIN_LOG_LEVEL=1

PUSHD %~dp0\..\nodetails\code
python %~dp0\app.py
POPD

ENDLOCAL