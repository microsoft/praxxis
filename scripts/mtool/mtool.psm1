function mtool {
    [CmdletBinding(DefaultParameterSetName = "Path", HelpURI = "")]
    param([string]$p1, [string]$p2, [string]$p3 , [string]$p4)

    $RUNNER= "$PSScriptRoot" + "\python\src\mtool\app.py"
    python $RUNNER $p1 $p2 $p3 $p4 
}