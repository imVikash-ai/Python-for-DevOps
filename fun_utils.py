import subprocess

# ✅ Fixed - using simple format without nested quotes
command_date   = 'powershell -command "Get-Date -UFormat \'%A, %B %d %Y %T\'"'

# OR even simpler - no format argument needed
command_date   = 'powershell -command "Get-Date"'

command_uptime = 'powershell -command "(Get-Date) - (gcim Win32_OperatingSystem).LastBootUpTime"'
command_cpu    = 'powershell -command "Get-CimInstance Win32_Processor | Select-Object -ExpandProperty LoadPercentage"'
command_ram    = 'powershell -command "$os = Get-CimInstance Win32_OperatingSystem; Write-Host Total: ([math]::Round($os.TotalVisibleMemorySize/1MB,2)) GB Free: ([math]::Round($os.FreePhysicalMemory/1MB,2)) GB"'

def check_cpu(command):
    subprocess.run(command, shell=True)

def check_date(command):
    subprocess.run(command, shell=True)

def check_ram(command):
    subprocess.run(command, shell=True)

def check_uptime(command):
    subprocess.run(command, shell=True)

# calling functions
check_date(command_date)
check_cpu(command_cpu)
check_ram(command_ram)
check_uptime(command_uptime)