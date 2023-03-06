## Write a script that will check if all AWS users have been created correctly as far as password, MFA set up and tag. Then, delete incorrect users and notify the security team by email. This script should run every day for security purposes.

## Attach policies for IAM and SES to the role of your lambda function in AWS.

## The script is below:

``` python
import boto3
from botocore.exceptions import ClientError
import schedule
import time

_iam = boto3.client('iam')
_incorrect_users=[]

def lambda_handler(event, context):
    def list_incorrect_users():
        """ fucntion to get the list of incorrect users """
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
            tags_list = user_tags['Tags']
            try:
                # Check if the user set the password
                _iam.get_login_profile(UserName=user)
            except ClientError as e:
                if (len(mfa['MFADevices'])==0) and (len(tags_list)==0):
                    # get users with no passwork, mfa and tags
                    _incorrect_users.append(user)
        return _incorrect_users

    incorrect_users_list = list_incorrect_users()
    users_deleted=[]
    def send_mail(list):
        """ function to send the list of incorrect users to the security team """
        # set a verified email address of security team 
        RECIPIENT = ["<SET A VERIFIED EMAIL OF SECURITY TEAM>"]
        # set your verified sender email address
        SENDER = "<SET A VERIFIED EMAIL OF SENDER>"
        SUBJECT = "Deletion of incorrect users"
        BODY_TEXT = (f"""
        Hello Security team, 
        This mail is to you notify that, the users in the list below have been deleted because they
        created their account without password, MFA and tag. 
        {list}""")           
        CHARSET = "UTF-8"
        # set your aws region
        AWS_REGION="<SET YOUR AWS REGION>"
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
        """ fucntion to delete all items linked to a user """

        # delete the password
        """ try:
            _iam.delete_login_profile(UserName=user)
        except ClientError as e:
            print(e)
        else:
            print(f"User password have been deleted for {user}!!") """
        # Delete access keys
        try:
            acces_keys_Ids=[]
            _list_access_keys= _iam.list_access_keys(UserName=user)
            for access_key in _list_access_keys['AccessKeyMetadata']:
                # get a list of access keys Ids
                acces_keys_Ids.append(access_key['AccessKeyId'])
            if len(acces_keys_Ids) != 0:
                for access_key_id in acces_keys_Ids:
                    # delete all access keys
                    _iam.delete_access_key(UserName=user, AccessKeyId=access_key_id)
                print(f"Access keys have been deleted for {user} !!")
            else:
                print(f"There are no access keys  for {user} !!")

        except ClientError as e:
            print(e)
        # Delete signing certificates
        try:
            certificate_ids=[]
            list_certificates= _iam.list_signing_certificates(UserName=user)
            for certificate in list_certificates['Certificates']:
                # get a list of certificate Ids
                certificate_ids.append(certificate['CertificateId'])
            if len(certificate_ids) != 0:
                for certificate_id in certificate_ids:
                    # delete all signing certificates
                    _iam.delete_signing_certificate(UserName=user, CertificateId=certificate_id)
                print(f"Signing certificates have been deleted for {user}!!")
            else:
                print(f"There are no signing certificates for {user}!!")
        except ClientError as e:
            print(e)
        
            
        # delete ssh public keys
        try:
            ssh_public_keys_Ids=[]
            _list_ssh_public_keys= _iam.list_ssh_public_keys(UserName=user)
            for key in _list_ssh_public_keys['SSHPublicKeys']:
                # get a list of ssh public keys Ids 
                ssh_public_keys_Ids.append(key['SSHPublicKeyId'])
            if len(ssh_public_keys_Ids) != 0:
                for key_id in ssh_public_keys_Ids:
                    # delete ssh public keys
                    _iam.delete_ssh_public_key(UserName=user, SSHPublicKeyId=key_id)
                print(f"SSH public keys have been deleted for {user}!!")
            else:
                print(f"There are no SSH public keys for {user}!!")
        except ClientError as e:
            print(e)

        # delete git credentials
        try:
            service_specific_credentials_Ids=[]
            _list_service_specific_credentials= _iam.list_service_specific_credentials(UserName=user)
            for key in _list_service_specific_credentials['ServiceSpecificCredentials']:
                # get a list of git credentials Ids
                service_specific_credentials_Ids.append(key['ServiceSpecificCredentialId'])
            if len(service_specific_credentials_Ids) != 0:
                for key_id in service_specific_credentials_Ids:
                    # delete git credentials
                    _iam.delete_service_specific_credential(UserName=user, ServiceSpecificCredentialId=key_id)
                print(f"Git credentials have been deleted for {user}!!")
            else:
                print(f"There are no Git credentials for {user}!!")
        except ClientError as e:
            print(e)

        # Delete mfa devices
        """ try:
            serial_numbers=[]
            _list_mfa_devices= _iam.list_mfa_devices(UserName=user)
            for key in _list_mfa_devices['MFADevices']:
                serial_numbers.append(key['SerialNumber'])
            if len(serial_numbers) != 0:
                for key_number in serial_numbers:
                    _iam.delete_virtual_mfa_device(UserName=user, SerialNumber=key_number)
                print(f"MFA devices have been deleted for {user}!!")
            else:
                print(f"There are no MFA devices associated to {user}!!")
        except ClientError as e:
            print(e) """

        # Delete inline policies
        try:
            policy_names=[]
            _list_user_policies= _iam.list_user_policies(UserName=user)
            for policy in _list_user_policies['PolicyNames']:
                # get a list of policy names
                policy_names.append(policy)
            if len(policy_names) != 0:
                for policy_name in policy_names:
                    # delete user policies
                    _iam.delete_user_policy(UserName=user, PolicyName=policy_name)
                print(f"Inline policies have been deleted for {user}!!")
            else:
                print(f"There are no inline policies associated to {user}!!")
        except ClientError as e:
            print(e)

        # Detach user managed policies
        try:
            policies_arn=[]
            _list_attached_user_policies= _iam.list_attached_user_policies(UserName=user)
            for key in _list_attached_user_policies['AttachedPolicies']:
                # get a list of policy arn
                policies_arn.append(key['PolicyArn'])
            if len(policies_arn) != 0:
                for key_arn in policies_arn:
                    # detach user from managed policies
                    _iam.detach_user_policy(UserName=user, PolicyArn=key_arn)
                print(f"User managed policies have been detached for {user}!!")
            else:
                print(f"There are no user managed policies to {user}!!")
        except ClientError as e:
            print(e)

        # Remove user from Groups
        try:
            group_names=[]
            _list_user_groups= _iam.list_groups_for_user(UserName=user)
            for group in _list_user_groups['Groups']:
                # get a list of group names
                group_names.append(group['GroupName'])
            if len(group_names) != 0:
                for group_name in group_names:
                    # remove user from groups
                    _iam.remove_user_from_group(UserName=user, GroupName=group_name)
                print(f"User has been removed for groups for {user}!!")
            else:
                print(f"There are no groups associated to {user}!!")
        except ClientError as e:
            print(e)

    # delete incorrect users
    for user in incorrect_users_list:
        delete_user_items(user)
        _iam.delete_user(UserName=user)
        users_deleted.append(user)
        send_mail(users_deleted)```

