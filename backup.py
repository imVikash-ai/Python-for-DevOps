import shutil
import os
import datetime

def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination ,f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file_name.replace('.tar.gz',""),'gztar',source)

#  Add r"" prefix to avoid escape character issues
source      = r"C:\Programming\AWS DEVOPS\Python"
destination = r"C:\Programming\AWS DEVOPS\Python\backups"

backup_files(source,destination)
