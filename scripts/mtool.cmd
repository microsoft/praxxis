@ECHO OFF

REM I have this as a .cmd/.sh file, because it gives the user something to do while python is taking 5 seconds
REM to cold boot (start)!!  First impressions count!   i.e. the user is reading the help, not noticing python is starting.

IF "%1" == "diag" (
    CALL python diag.py %2
) ELSE IF "%1" == "diagnose" (
    CALL python diag.py %2
) ELSE IF "%1" == "run" (
    CALL python run.py %2 %3
) ELSE IF "%1" == "r" (
    CALL python run.py %2 %3
) ELSE IF "%1" == "open" (
    CALL python open.py %2
) ELSE IF "%1" == "o" (
    CALL python open.py %2
) ELSE IF "%1" == "search" (
    CALL python search.py %2
) ELSE IF "%1" == "s" (
    CALL python search.py %2
) ELSE IF "%1" == "list" (
    CALL python list.py
) ELSE IF "%1" == "l" (
    CALL python list.py
) ELSE IF "%1" == "h" (
    CALL python history.py
) ELSE IF "%1" == "history" (
    CALL python history.py
) ELSE IF "%1" == "whatnext" (
    ECHO coming soon...
) ELSE IF "%1" == "n" (
    ECHO coming soon...
) ELSE IF "%1" == "scene" (
    IF '%2' == 'new' ( 
        CALL python new-scene.py %3 %4
    ) ELSE IF '%2' == 'end' ( 
        CALL python end-scene.py %3 
    ) ELSE IF '%2' == 'change' ( 
        CALL python change-scene.py %3 %4
    ) ELSE IF '%2' == 'resume' ( 
        CALL python resume-scene.py %3 
    ) ELSE IF '%2' == 'delete' ( 
        CALL python delete-scene.py %3 
    ) ELSE IF '%2' == 'list' (
        CALL python list-scene.py
    ) ELSE (
        ECHO "Invalid 'scene' option" 
    )
) ELSE IF "%1" == "ns" (
    python new-scene.py %2
) ELSE IF "%1" == "es" (
    python end-scene.py %2
) ELSE IF "%1" == "cs" (
    python change-scene.py %2 %3
) ELSE IF "%1" == "ss" (
    python change-scene.py %2 %3
) ELSE IF "%1" == "rs" (
    python resume-scene.py %2
) ELSE IF "%1" == "ds" (
    python delete-scene.py %2
) ELSE IF "%1" == "ls" (
    python list-scene.py
) ELSE IF "%1" == "library" (
    IF '%2' == 'add' ( 
        ECHO coming soon...
    ) ELSE IF '%2' == 'remove' ( 
        ECHO coming soon...
    ) ELSE IF '%2' == 'list' ( 
        CALL python list-libraries.py
    ) ELSE (
        ECHO "Invalid 'library' option" 
    )
) ELSE IF "%1" == "ll" (
    python list-libraries.py
) ELSE IF "%1" == "env" (
    IF '%2' == 'set' ( 
        CALL python set-env.py %2 %3
    ) ELSE IF '%2' == 'delete' ( 
        CALL python delete-env.py %2 
    ) ELSE IF '%2' == 'list' ( 
        CALL python list-env.py
    ) ELSE IF '%2' == 'search' ( 
        ECHO coming soon...
    ) ELSE (
        ECHO "Invalid 'env' option" 
    )
) ELSE IF "%1" == "se" (
    python set-env.py %2 %3
) ELSE IF "%1" == "de" (
    python delete-env.py %2
) ELSE IF "%1" == "le" (
    python list-env.py
) ELSE IF "%1" NEQ "" (
    REM This clause must be the last ELSE IF

    python run.py %*
) ELSE (

    ECHO Welcome to m.
    ECHO.
    ECHO Notebook:
    ECHO     list           l : list notebooks to run, by ordinal.
    ECHO     open           o : open notebook in Azure Data Studio e.g. m open SOP027.
    ECHO     run            r : run notebook e.g. m run SOP027.
    ECHO     diag             : diagnose current state against TSG pre-conditions. e.g. m diag.
    ECHO     search         s : search for notebooks matching search term e.g. m search "install".
    ECHO     [n]              : runs the nth notebook in the list, e.g. m 4, runs the 4. item in m list
    ECHO.
    ECHO     history        h : of what you've done, in the current scene, e.g. m h
    ECHO     whatnext       n : model based prediction of what to do next, in the current scene, e.g. m n
    ECHO.
    ECHO Scene:
    ECHO     scene new     ns : new scene, a new thing to do.
    ECHO     scene end     es : end scene, prevent accidently adding to current scene.
    ECHO     scene change  cs : change scene, to what to do now.
    ECHO     scene switch  ss : switch scene, same as above, i.e. same as 'cs' above.
    ECHO     scene resume  rs : resume scene, resume current scene previously ended.
    ECHO     scene delete  ds : delete scene.
    ECHO     scene list    ls : list scenes, i.e. all the things you're doing.
    ECHO.
    ECHO Environment:
    ECHO     env set       se : set environment variable for current scene. e.g. m se 1 "~/src"
    ECHO     env delete    de : delete environment variable for current scene.
    ECHO     env search       : search for environment variable names. e.g. m env search aks
    ECHO     env list      le : list environment variables.
    ECHO.
    ECHO Library:
    ECHO     library add      : install library of notebooks to mtool
    ECHO     library remove   : remove library of notebooks mtool
    ECHO     library list  ll : list libraries currently installed.
    ECHO.
    ECHO     --html           : Display executed notebook in web browser
    ECHO     --yes            : NYI - do not prompt before running a notebook which has side affects!

    python ../runner.py
)