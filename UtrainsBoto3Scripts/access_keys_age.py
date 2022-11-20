#!/bin/python
import boto3
from datetime import date

client = boto3.client('iam')
username = "<SET YOUR USERNAME HERE>"
response = client.list_access_keys(UserName=username)
accesskeydate = response['AccessKeyMetadata'][0]['CreateDate'].date()
currentdate = date.today()
keys_age = currentdate - accesskeydate
print (f"The access date key from the user {username} is: {accesskeydate}")
print (f"The access key age is: {keys_age.days}")
