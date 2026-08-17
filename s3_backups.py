# boto3 -> used to do AWS tasks using python

import boto3

s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_buckets(s3,bucket_name,region):
    s3.create_bucket(Bucket = bucket_name,CreateBucketConfiguration = {'LocationConstraint':region})
    print("Bucket created successfully")

def upload_backups(s3,file_name,bucket_name,key_name):
    data = open(file_name,'rb')
    s3.Bucket(bucket_name).put_object(Key = key_name,Body = data)
    print("Backup uploaded successfully!")

bucket_name = "python-for-devops-junoon1"
region = 'us-east-2'
# create_buckets(s3)
# show_buckets(s3)

file_name = r"C:\Programming\AWS DEVOPS\Python\backups\backup_2026-08-17.tar.gz" 

upload_backups(s3,file_name,bucket_name,"my-backup.tar.gz")