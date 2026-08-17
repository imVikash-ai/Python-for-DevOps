import subprocess

# Disk Space
subprocess.run(['powershell', '-command', 'Get-PSDrive -PSProvider FileSystem'])

# Uptime
subprocess.run(['powershell', '-command', '(Get-Date) - (gcim Win32_OperatingSystem).LastBootUpTime'])

# RAM Total
subprocess.run(['powershell', '-command', '(Get-CimInstance Win32_PhysicalMemory | Measure-Object -Property Capacity -Sum).Sum / 1GB'])

# RAM Usage (Free vs Used)
subprocess.run(['powershell', '-command', '$os = Get-CimInstance Win32_OperatingSystem; "Total: {0}GB, Free: {1}GB" -f [math]::Round($os.TotalVisibleMemorySize/1MB,2), [math]::Round($os.FreePhysicalMemory/1MB,2)'])