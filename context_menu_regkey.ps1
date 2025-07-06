$pythonPath = "C:\Python39\python.exe"
$scriptPath = "C:\Tools\hash_file.py"

New-Item -Path "HKCR:\*\shell\HashThisFile" -Force | Out-Null
Set-ItemProperty -Path "HKCR:\*\shell\HashThisFile" -Name "(default)" -Value "Hash This File"
Set-ItemProperty -Path "HKCR:\*\shell\HashThisFile" -Name "Icon" -Value $pythonPath
New-Item -Path "HKCR:\*\shell\HashThisFile\command" -Force | Out-Null
Set-ItemProperty -Path "HKCR:\*\shell\HashThisFile\command" -Name "(default)" -Value "`"$pythonPath`" `"$scriptPath`" `"%1`""
