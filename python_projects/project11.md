## Write a script that will check if all AWS users have been created correctly as far as password, MFA set up and tag. This script should run every day for security purposes.

## The script is below:

``` python
import boto3
from botocore.exceptions import ClientError
import schedule
import time

# set your region
AWS_REGION="af-south-1"
_iam = boto3.client('iam')
_uncorrect_users=[]

def list_uncorrect_users():
    _iam_users = []
    users = _iam.list_users()
    # get all iam user names
    for i in users['Users']:
        _iam_users.append(i['UserName'])

    for user in _iam_users:
        # get mfa devices associated to the user
        mfa =_iam.list_mfa_devices(UserName=user)
        # get the list of tags attached to a user
        user_tags= _iam.list_user_tags(UserName=user)
        email_tag = list(filter(lambda tag: tag['Key'] == 'email', user_tags['Tags']))
        try:
            # Check if the user set the password
            _iam.get_login_profile(UserName=user)
        except ClientError as e:
            if (len(mfa['MFADevices'])==0) and (len(email_tag)==0):
                _uncorrect_users.append(user)
                # print(user)
                # print(mfa['MFADevices'])
                # print("******************")
    return _uncorrect_users

uncorrect_users_list = list_uncorrect_users()
users_deleted=[]
def send_mail(list):
    # set a verified email address of security team <SET A VERIFIED EMAIL OF SECURITY TEAM>
    RECIPIENT = ["estephe.kana@utrains.org"]
    # set your verified sender email address
    SENDER = "estephe.kana@utrains.org"
    SUBJECT = "Deletion of Uncorrect users"
    BODY_TEXT = (f"""
    Hello Security team, 
    This mail is to you notify that, the users in the list below have been deleted because they
    created their account without password, MFA and tag. 
    {list}""")           
    CHARSET = "UTF-8"
    ses_client = boto3.client('ses', region_name=AWS_REGION)
    try:
        response = ses_client.send_email(
            Destination={
                'ToAddresses': RECIPIENT,
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(f"Email sent! Message ID: {response['MessageId']}")

def delete_user_items(user):
    # delete the password
    try:
        _iam.delete_login_profile(UserName=user)
    except ClientError as e:
        print(e)
    else:
        print("User password have been deleted !!")
    # Delete access keys
    try:
        paginator = _iam.get_paginator('list_access_keys')
        for response in paginator.paginate(UserName=user):
            access_id=response['AccessKeyMetadata'][0]['AccessKeyId']
            _iam.delete_access_key(AccessKeyId=access_id, UserName=user)
    except ClientError as e:
        print(e)
    else:
        print("Access keys have been deleted !!")
    # Delete signing certificates
    try:
        certificate_ids=[]
        list_certificates= _iam.list_signing_certificates(UserName=user)
        for certificate in list_certificates['Certificates']:
            certificate_ids.append(certificate['CertificateId'])
        for certificate_id in certificate_ids:
            _iam.delete_signing_certificate(UserName=user, CertificateId=certificate_id)
    except ClientError as e:
        print(e)
    else:
        print("Signing certificates have been deleted !!")
    # delete ssh public keys
    try:
        ssh_public_keys_Ids=[]
        _list_ssh_public_keys= _iam.list_ssh_public_keys(UserName=user)
        for key in _list_ssh_public_keys['SSHPublicKeys']:
            ssh_public_keys_Ids.append(key['SSHPublicKeyId'])
        for key_id in ssh_public_keys_Ids:
            _iam.delete_ssh_public_key(UserName=user, SSHPublicKeyId=key_id)
    except ClientError as e:
        print(e)
    else:
        print("SSH public keys have been deleted !!")

    # delete git credentials
    try:
        service_specific_credentials_Ids=[]
        _list_service_specific_credentials= _iam.list_service_specific_credentials(UserName=user)
        for key in _list_service_specific_credentials['ServiceSpecificCredentials']:
            service_specific_credentials_Ids.append(key['ServiceSpecificCredentialId'])
        for key_id in service_specific_credentials_Ids:
            _iam.delete_service_specific_credential(UserName=user, ServiceSpecificCredentialId=key_id)
    except ClientError as e:
        print(e)
    else:
        print("Git credentials have been deleted !!")

    # Delete mfa devices
    try:
        serial_numbers=[]
        _list_mfa_devices= _iam.list_mfa_devices(UserName=user)
        for key in _list_mfa_devices['MFADevices']:
            serial_numbers.append(key['SerialNumber'])
        for key_number in serial_numbers:
            _iam.delete_virtual_mfa_device(UserName=user, SerialNumber=key_number)
    except ClientError as e:
        print(e)
    else:
        print("MFA devices have been deleted !!")

    # Delete inline policies
    try:
        
        _list_user_policies= _iam.list_user_policies(UserName=user)
        for policy_name in _list_user_policies['PolicyNames']:
            _iam.delete_user_policy(UserName=user, PolicyName=policy_name)
    except ClientError as e:
        print(e)
    else:
        print("Inline policies have been deleted !!")

    # Detach user managed policies
    try:
        policies_arn=[]
        _list_attached_user_policies= _iam.list_attached_user_policies(UserName=user)
        for key in _list_attached_user_policies['AttachedPolicies']:
            policies_arn.append(key['PolicyArn'])
        for key_arn in policies_arn:
            _iam.detach_user_policy(UserName=user, PolicyArn=key_arn)
    except ClientError as e:
        print(e)
    else:
        print("User managed policies have been detached !!")

    # Remove user from Groups
    try:
        group_names=[]
        _list_user_groups= _iam.list_groups_for_user(UserName=user)
        for group in _list_user_groups['Groups']:
            group_names.append(group['GroupName'])
        for group_name in group_names:
            _iam.remove_user_from_group(UserName=user, GroupName=group_name)
    except ClientError as e:
        print(e)
    else:
        print("User has been removed for groups !!")

for user in uncorrect_users_list:
    """ function to delete uncorrect users """
    if user=='python-kana':
        delete_user_items(user)
        _iam.delete_user(UserName=user)
        users_deleted.append(user)
        send_mail(users_deleted)
    else:
        print(user)
    """ user_info=_iam.get_user(UserName=user)
    print(user_info) """
```

