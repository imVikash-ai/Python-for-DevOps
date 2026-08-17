# 🐍 Python for DevOps

A hands-on collection of Python scripts for learning and implementing real-world DevOps automation tasks — covering system utilities, cloud backups, AWS S3, and Terraform automation.

---

---

## 🚀 Scripts Overview

### 🔰 Python Basics

| File | Description |
|------|-------------|
| `hello.py` | Hello World — getting started with Python |
| `calculator.py` | Basic arithmetic operations |
| `conditional.py` | `if/elif/else` conditions |
| `loops.py` | `for` and `while` loops |

---

### 🖥️ System Utilities

#### `utils.py`
Checks system health — disk space, uptime, and RAM using OS commands.

```python
import os

# Linux / Mac
print(os.system('df -h'))           # Disk space
print(os.system('uptime'))          # Uptime & load average
print(os.system('sysctl hw.memsize'))  # RAM for macOS
print(os.system('free -h'))         # RAM for Linux
```

> 💡 **Windows Users:** Use `subprocess` with PowerShell commands instead of `os.system`.
> ```python
> import subprocess
> subprocess.run(['powershell', '-command', 'Get-PSDrive -PSProvider FileSystem'])
> subprocess.run(['powershell', '-command', 'Get-CimInstance Win32_Processor | Select-Object -ExpandProperty LoadPercentage'])
> ```

---

#### `fun_utils.py`
Wraps system commands in reusable functions.

```python
import os

def check_cpu(command):
    print(os.system(command))

def check_date(command):
    print(os.system(command))

def check_ram(command):
    print(os.system(command))

def check_uptime(command):
    print(os.system(command))

check_date("date")
```

---

### 💾 Local Backup

#### `backup.py`
Creates a `.tar.gz` archive of a source directory and saves it with a date-stamped filename.

```python
import shutil
import os
import datetime

def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file_name, 'gztar', source)

source      = r"C:\Programming\AWS DEVOPS\Python"        # Windows path
destination = r"C:\Programming\AWS DEVOPS\Python\backups"

os.makedirs(destination, exist_ok=True)
backup_files(source, destination)
```

> ⚠️ **Windows Tip:** Always use raw strings `r"..."` for Windows paths.  
> `\b`, `\n`, `\t` in paths are interpreted as special characters — `r""` prevents this.

---

### ☁️ AWS S3 Backup

#### `s3_backups.py`
Creates an S3 bucket, lists all buckets, and uploads a local backup file.

**Prerequisites:**
```bash
pip install boto3
aws configure   # set your AWS credentials
```

```python
import boto3

s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_buckets(s3):
    s3.create_bucket(
        Bucket="python-for-devops-junoon1",   # must be lowercase!
        CreateBucketConfiguration={'LocationConstraint': 'us-east-2'}
    )
    print("Bucket created successfully")

def upload_backups(s3, file_name, bucket_name, key_name):
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup uploaded successfully!")

bucket_name = "python-for-devops-junoon1"
file_name   = r"C:\Programming\AWS DEVOPS\Python\backups\backup_2026-08-17.tar.gz"

create_buckets(s3)
show_buckets(s3)
upload_backups(s3, file_name, bucket_name, "my-backup.tar.gz")
```

---

### 🏗️ Terraform Automation

#### `terraform.py`
Runs Terraform CLI commands programmatically using Python's `subprocess`.

```python
import subprocess

def terraform_run(command):
    proces = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
    return proces.stdout.decode()

directory = r"C:\Programming\AWS DEVOPS\Python\terraform"

# Run terraform init
command = f'terraform -chdir="{directory}" init'
print(command)
terraform_run(command)
```

---

## 🛠️ Requirements

```bash
pip install boto3
```

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| `boto3` | AWS SDK for S3 operations |
| `subprocess` | Run shell & PowerShell commands |
| `shutil` | Create local archives |
| `datetime` | Date-stamped backup filenames |
| Terraform CLI | Infrastructure automation |
| AWS CLI | Cloud credentials setup |

---

## ⚙️ Setup & Usage

```bash
# 1. Clone the repo
git clone https://github.com/imVikash-ai/Python-for-DevOps.git
cd Python-for-DevOps

# 2. Install dependencies
pip install boto3

# 3. Configure AWS credentials
aws configure

# 4. Run any script
python utils.py
python backup.py
python s3_backups.py
python terraform.py
```

---

## 👨‍💻 Author

**Vikash** — [@imVikash-ai](https://github.com/imVikash-ai)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).