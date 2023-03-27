import boto3

# Interacting with Boto3 and Amazon Identity and Access Management (IAM)

# create a new IAM user

def create_iam_user(username):
    iam_client = boto3.client("iam")
    response = iam_client.create_user(UserName=username)
    print(response)

#create_iam_user('utrains')

# get a list of all IAM users
def list_iam_users():
    iam_client = boto3.client("iam")
    paginator = iam_client.get_paginator('list_users')
    for response in paginator.paginate():
        for user in response["Users"]:
            print(f"Username: {user['UserName']}, Arn: {user['Arn']}")

#list_iam_users()

# update the name of IAM user
def update_user(old_user_name, new_user_name):
    iam_client = boto3.client('iam')
    # Update a user name
    response = iam_client.update_user(
        UserName=old_user_name,
        NewUserName=new_user_name
    )
    print(response)

#update_user('utrains','python-utrains')

# create an IAM policy
import json

def create_iam_policy():
    # Create IAM client
    iam_client = boto3.client('iam')

    # Create a policy
    my_managed_policy = {"Version": "2012-10-17",
        "Statement": [
            {"Effect": "Allow","Action": ["dynamodb:GetItem","dynamodb:Scan",],
                "Resource": "*"
            }
        ]
    }
    response = iam_client.create_policy(
        PolicyName='testDynamoDBPolicy',
        PolicyDocument=json.dumps(my_managed_policy)
    )
    print(response)

#create_iam_policy()

# list all IAM policies of AWS account

def list_policies():
    iam_client = boto3.client("iam")
    paginator = iam_client.get_paginator('list_policies')
    for response in paginator.paginate(Scope="Local"):
        for policy in response["Policies"]:
            print(f"Policy Name: {policy['PolicyName']} ARN: {policy['Arn']}")

#list_policies()

# Attach a specific policy to a specific user
def attach_user_policy(username, policy_arn):
    iam_client = boto3.client("iam")
    response = iam_client.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    print(response)

#attach_user_policy('python-utrains','arn:aws:iam::076892551558:policy/testDynamoDBPolicy')
