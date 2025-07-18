#Look into PATH variable if possible
$pythonPath = "C:\Users\Fahim\AppData\Local\Programs\Python\Python312\python.exe"


$scriptPath = "D:\5. Code\Malware_hashcheck\test_script.py"

#New-PSDrive -Name HKCR -PSProvider Registry -Root HKEY_CLASSES_ROOT
New-Item -Path "HKCR:\*\shell\HashThisFile" -Force | Out-Null
Set-ItemProperty -Path "HKCR:\*\shell\HashThisFile" -Name "(default)" -Value "Hash This File"
#Set-ItemProperty -Path "HKCR:\*\shell\HashThisFile" -Name "Icon" -Value $pythonPath
#New-Item -Path "HKCR:\*\shell\HashThisFile\command" -Force | Out-Null
#Set-ItemProperty -Path "HKCR:\*\shell\HashThisFile\command" -Name "(default)" -Value "`"$pythonPath`" `"$scriptPath`" `"%1`""
