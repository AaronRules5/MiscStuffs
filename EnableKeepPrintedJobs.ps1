param([switch]$Admin)
function isAdmin {
    return (New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())).isInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
}

if ((isAdmin) -eq $false){
    if ($Admin){
        exit
    }
    else{
        Start-Process powershell.exe -Verb RunAs -ArgumentList ('-noprofile -file "{0}" -Admin' -f ($myInvocation.MyCommand.Definition))
    }
    exit
}

ForEach ($Printer in Get-Printer){
    Set-Printer -ErrorAction 'silentlycontinue' -Name $Printer.Name -KeepPrintedJobs $True
    if ($?){
        Write-Host -ForegroundColor green "Successfully enabled KeepPrintedJobs for printer: " $Printer.Name
    } else{
        Write-Host -ForegroundColor red "Could not enable keepPrintedJobs for printer: " $Printer.Name
    }
}

Write-Host "Press any key to exit..."
$x = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")