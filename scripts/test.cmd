@ECHO OFF
set "MTOOL_DIR=../mtool"
set "ENVIRONMENT_DIR=/environment"
set "CLI_DIR=/cli"
set "LIBRARY_DIR=/library"
set "NOTEBOOK_DIR=/notebook"
set "PANSOP_DIR=/pansop"
set "SCENE_DIR=/scene"
set "UTIL_DIR=/util"

set "ENVIRONMENT=%MTOOL_DIR%%ENVIRONMENT_DIR%"
set "CLI=%MTOOL_DIR%%CLI_DIR%"
set "LIBRARY=%MTOOL_DIR%%LIBRARY_DIR%"
set "NOTEBOOK=%MTOOL_DIR%%NOTEBOOK_DIR%"
set "PANSOP=%MTOOL_DIR%%PANSOP_DIR%"
set "SCENE=%MTOOL_DIR%%SCENE_DIR%"
set "UTIL=%MTOOL_DIR%%UTIL_DIR%"

echo %ENVIRONMENT%
echo %CLI%
echo %LIBRARY%
echo %NOTEBOOK%
echo %PANSOP%
echo %SCENE%
echo %UTIL%