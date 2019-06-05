mklink /D "%UserProfile%\Documents\WindowsPowerShell\Modules\mtool" "%~dp0%"
mklink /D "%UserProfile%\Documents\WindowsPowerShell\Modules\mtool\python\mtool" "%~dp0%..\..\mtool"
mklink /D "%UserProfile%\Documents\WindowsPowerShell\Modules\mtool\python\library" "%~dp0%..\..\library"
mklink  "%UserProfile%\Documents\WindowsPowerShell\Modules\mtool\python\runner.py" "%~dp0%..\..\runner.py"

powershell -Command "Import-module -name mtool"
pause