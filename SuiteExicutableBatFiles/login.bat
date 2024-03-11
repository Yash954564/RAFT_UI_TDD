
@echo off

set currentDir=%cd%
echo %currentDir%
cd..

pytest ./TestScripts/test_login.py --alluredir=ExecutionReports/Login/"%date:/=-%"

