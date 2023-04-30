# session: AWS management Console

import boto3
aws_mg_con=boto3.session.Session(profile_name='profile_name')
iam_con=aws_mg_con.resource('iam')

# list all iam users
# for each user in iam_con.all():
# print(each_user.name)

print(dir(aws_mg_con))