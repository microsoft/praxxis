mklink /D "%UserProfile%\Documents\WindowsPowerShell\Modules\mtool" "%~dp0%"
mklink /D "%UserProfile%\Documents\WindowsPowerShell\Modules\mtool\python\src" "%~dp0%..\..\src"
mklink /D "%UserProfile%\Documents\WindowsPowerShell\Modules\mtool\python\library" "%~dp0%..\..\library"

powershell -Command "Import-module -name mtool"
pause