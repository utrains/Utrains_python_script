## Write a script that will check if all AWS users have been created correctly as far as password, MFA set up and tag. This script should run every day for security purposes.

## The script is below:

``` python
import boto3
from botocore.exceptions import ClientError
import schedule
import time

def list_uncorrect_users():
    _iam = boto3.client('iam')
    users = _iam.list_users()
    _iam_users = []
    _uncorrect_users=[]
    for i in users['Users']:
        _iam_users.append(i['UserName'])

    for users in _iam_users:
        mfa =_iam.list_mfa_devices(UserName=users)
        users_tags= _iam.list_user_tags(UserName=users)
        email_tag = list(filter(lambda tag: tag['Key'] == 'email', users_tags['Tags']))
        try:
            user_profile=_iam.get_login_profile(UserName=users)
            user_profile_date=user_profile['LoginProfile']['CreateDate']
            #print(users, user_profile_date)
        except ClientError as e:
            if (len(mfa['MFADevices'])==0) and (len(email_tag)==0):
                _uncorrect_users.append(users)
                print(users)
                #print(mfa['MFADevices'])
                print("******************")
    print(_uncorrect_users)
    return _uncorrect_users
    # delete uncorrect iam users
    for user in list_uncorrect_users():
        _iam.delete_user(UserName=user)
