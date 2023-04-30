# session: AWS management Console

import boto3
aws_mg_con=boto3.session.Session(profile_name='profile_name')
#iam_con=aws_mg_con.resource('iam')

# list all iam users
# for each user in iam_con.all():
# print(each_user.name)

#example 
print(aws_mg_con.get_available_resources()) 

# client
iam_con=aws_mg_con.client(service_name='iam', region_name='us-east-1')

# for loop
for each_user in iam_con.list_users()["User"]:
    print(each_user['UserName'])