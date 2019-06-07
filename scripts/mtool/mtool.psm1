function mtool {
    [CmdletBinding(DefaultParameterSetName = "Path", HelpURI = "")]
    param([string]$p1, [string]$p2, [string]$p3 , [string]$p4)

    begin{
        $RUNNER= "$PSScriptRoot" + "\python\src\mtool\app.py"
        $DIAGNOSE = "diagnose"
        $RUN_NOTEBOOK = "run_notebook"
        $OPEN_NOTEBOOK = "open_notebook"
        $SEARCH_NOTEBOOK = "search_notebook"
        $LIST_NOTEBOOK = "list_notebook"
        $HISTORY = "history"
        $NEXT_NOTEBOOK = "next_notebook"
        $NEW_SCENE = "new_scene"
        $END_SCENE = "end_scene"
        $CHANGE_SCENE = "change_scene"
        $RESUME_SCENE = "resume_scene"
        $DELETE_SCENE = "delete_scene"
        $LIST_SCENE = "list_scene"
        $REMOVE_LIBRARY = "remove_library"
        $ADD_LIBRARY = "add_library"
        $LIST_LIBRARY = "list_library"
        $SET_ENV = "set_env"
        $DELETE_ENV = "delete_env"
        $LIST_ENV = "list_env"
        
        if ("$p1" -eq "diag") {
            CALL python $RUNNER $DIAGNOSE $p2
        } elseif ("$p1" -eq "diagnose" ) {
            CALL python $RUNNER $DIAGNOSE $p2
        } elseif ("$p1" -eq "run") {
            CALL python $RUNNER $RUN_NOTEBOOK $p2 $p3
        } elseif ("$p1" -eq "r") {
            CALL python $RUNNER $RUN_NOTEBOOK $p2 $p3
        } elseif ("$p1" -eq "open") {
            CALL python $RUNNER $OPEN_NOTEBOOK $p2
        } elseif ("$p1" -eq "o") {
            CALL python $RUNNER $OPEN_NOTEBOOK $p2
        } elseif ("$p1" -eq "search") {
            CALL python $RUNNER $SEARCH_NOTEBOOK $p2
        } elseif ("$p1" -eq "s") {
            CALL python $RUNNER $SEARCH_NOTEBOOK $p2
        } elseif ("$p1" -eq "list") {
            CALL python $RUNNER $LIST_NOTEBOOK
        } elseif ("$p1" -eq "l") {
            CALL python $RUNNER $LIST_NOTEBOOK
        } elseif ("$p1" -eq "h") {
            CALL python $RUNNER $HISTORY
        } elseif ("$p1" -eq "history") {
            CALL python $RUNNER $HISTORY
        } elseif ("$p1" -eq "whatnext") {
            Write-Output coming soon...
        } elseif ("$p1" -eq "n") {
            Write-Output coming soon...
        } elseif ("$p1" -eq "scene") {
            if ('$p2' -eq 'new') { 
                CALL python $RUNNER $NEW_SCENE $p3 $p4
            } elseif ('$p2' -eq 'end') { 
                CALL python $RUNNER $END_SCENE $p3 
            } elseif ('$p2' -eq 'change') { 
                CALL python $RUNNER $CHANGE_SCENE $p3 $p4
            } elseif ('$p2' -eq 'resume') { 
                CALL python $RUNNER $RESUME_SCENE $p3 
            } elseif ('$p2' -eq 'delete') { 
                CALL python $RUNNER $DELETE_SCENE $p3 
            } elseif ('$p2' -eq 'list'){
                CALL python $RUNNER $LIST_SCENE
            } else {
                Write-Output "Invalid 'scene' option" 
            }
        } elseif ("$p1" -eq "ns") {
            python $RUNNER $NEW_SCENE $p2
        } elseif ("$p1" -eq "es") {
            python $RUNNER $END_SCENE $p2
        } elseif ("$p1" -eq "cs") {
            python $RUNNER $CHANGE_SCENE $p2 $p3
        } elseif ("$p1" -eq "ss") {
            python $RUNNER $CHANGE_SCENE $p2 $p3
        } elseif ("$p1" -eq "rs") {
            python $RUNNER $RESUME_SCENE $p2
        } elseif ("$p1" -eq "ds") {
            python $RUNNER $DELETE_SCENE $p2
        } elseif ("$p1" -eq "ls") {
            python $RUNNER $LIST_SCENE
        } elseif ("$p1" -eq "library") {
            if ('$p2' -eq 'add') { 
                Write-Output coming soon...
            } elseif ('$p2' -eq 'remove') { 
                Write-Output coming soon...
            } elseif ('$p2' -eq 'list') { 
                CALL python $RUNNER $LIST_LIBRARY
            } else {
                Write-Output "Invalid 'library' option" 
            }
        } elseif ("$p1" -eq "ll") {
            python $RUNNER $LIST_LIBRARY
        } elseif ("$p1" -eq "env") {
            if ('$p2' -eq 'set') { 
                CALL python $RUNNER $SET_ENV $p2 $p3
            } elseif ('$p2' -eq 'delete') { 
                CALL python $RUNNER $DELETE_ENV $p2 
            } elseif ('$p2' -eq 'list') { 
                CALL python $RUNNER $LIST_ENV
            } elseif ('$p2' -eq 'search') { 
                Write-Output coming soon...
            } else {
                Write-Output "Invalid 'env' option" 
            }
        } elseif ("$p1" -eq "se") {
            python $RUNNER $SET_ENV $p2 $p3
        } elseif ("$p1" -eq "de") {
            python $RUNNER $DELETE_ENV $p2
        } elseif ("$p1" -eq "le") {
            python $RUNNER $LIST_ENV
        } elseif ("$p1" -eq ""){
            python $RUNNER $RUN_NOTEBOOK %*
        } else {
        
            Write-Output "Welcome to m.
        
        Notebook:
        list           l : list notebooks to run, by ordinal.
        open           o : open notebook in Azure Data Studio e.g. m open SOP027.
            run            r : run notebook e.g. m run SOP027.
            diag             : diagnose current state against TSG pre-conditions. e.g. m diag.
            search         s : search for notebooks matching search term e.g. m search 'install'.
            [n]              : runs the nth notebook in the list, e.g. m 4, runs the 4. item in m list
        
            history        h : of what you've done, in the current scene, e.g. m h
            whatnext       n : model based prediction of what to do next, in the current scene, e.g. m n
        
        Scene:
            scene new     ns : new scene, a new thing to do.
            scene end     es : end scene, prevent accidently adding to current scene.
            scene change  cs : change scene, to what to do now.
            scene switch  ss : switch scene, same as above, i.e. same as 'cs' above.
            scene resume  rs : resume scene, resume current scene previously ended.
            scene delete  ds : delete scene.
            scene list    ls : list scenes, i.e. all the things you're doing.
        
        Environment:
            env set       se : set environment variable for current scene. e.g. m se 1 '~/src'
            env delete    de : delete environment variable for current scene.
            env search       : search for environment variable names. e.g. m env search aks
            env list      le : list environment variables.
        
        Library:
            library add      : install library of notebooks to mtool
            library remove   : remove library of notebooks mtool
            library list  ll : list libraries currently installed.
        
            --html           : Display executed notebook in web browser
            --yes            : NYI - do not prompt before running a notebook which has side affects!"
        
            python $RUNNER
        }
    }
}
Set-Alias -Name m -Value mtool
Export-ModuleMember -Function mtool -Alias m
