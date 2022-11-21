import boto3

# set your region
AWS_REGION="<SET YOUR REGION>"
iam_client=boto3.client("iam",region_name=AWS_REGION)

print("####### List of all IAM Users with details #######")
for each_user in iam_client.list_users()['Users']:
    print(f"{each_user['UserName']} \t {each_user['Arn']}")
