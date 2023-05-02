import boto3

s3 = boto3.client('s3')

bucket_name = 'codebuild-beta'
object_key = 'index.html'
file_path = 'index.html'
acl = 'public-read'
content_type = 'text/html'

with open(file_path, 'rb') as f:
    s3.put_object(Bucket=bucket_name, Key=object_key, Body=f, ACL=acl, ContentType=content_type)
