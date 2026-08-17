import subprocess
def terraform_run(command):
    proces = subprocess.run(command,shell = True, check= True ,stdout=subprocess.PIPE)

    return proces.stdout.decode()

directory = r"C:\Programming\AWS DEVOPS\Python\terraform"
# command = f'terraform -chdir="{directory}" init'
command = f'terraform -chdir="{directory}" plan'


print(command)
terraform_run(command)