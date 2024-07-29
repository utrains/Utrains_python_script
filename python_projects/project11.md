## Write a script that will check if all AWS users have been created correctly as far as password, MFA set up and tag. Then, delete incorrect users and notify the security team by email. This script should run every day for security purposes.

## Attach policies for IAM and SES to the role of your lambda function in AWS.

## The script is below:

``` python
import boto3
from botocore.exceptions import ClientError

iam_client = boto3.client('iam')
incorrect_users=[]
users_deleted=[]

def lambda_handler(event, context):

    def list_incorrect_users():
        """ function to get the list of incorrect users """
        iam_users = []
        users = iam_client.list_users()
        # get all IAM user names
        for i in users['Users']:
            iam_users.append(i['UserName'])

        for user_name in iam_users:
            try:
                # Get MFA devices associated with the user
                mfa_devices = iam_client.list_mfa_devices(UserName=user_name)
                mfa_count = len(mfa_devices['MFADevices'])
                
                # Get the list of tags attached to the user
                user_tags = iam_client.list_user_tags(UserName=user_name)
                tags_list = user_tags['Tags']
                
                # Check if the user has a login profile (password)
                iam_client.get_login_profile(UserName=user_name)
                login_profile_exists = True
            except ClientError as e:
                login_profile_exists = False
            
            if not login_profile_exists and mfa_count == 0 and not tags_list:
                incorrect_users.append(user_name)
        return incorrect_users
    

    def send_mail(user_list):
        """ function to send the list of incorrect users to the security team """
        # set a verified email address for security team 
        RECIPIENT = ["<SET A VERIFIED EMAIL OF SECURITY TEAM>"]
        # set your verified sender email address
        SENDER = "<SET A VERIFIED EMAIL OF SENDER>"
        SUBJECT = "Notification: Deletion of Incorrect IAM Users"
        BODY_TEXT = (f"""
        Hello Security team,
         
        This email is to inform you that the following IAM users have been identified as incorrect and have been deleted from the AWS account.
        The deletion was necessary because these users were created without meeting the required security configurations, including a password, MFA, and user tags.
                     
        Below is the list of deleted users:
    
        {', '.join(user_list)}

        If you have any questions or need further details, please do not hesitate to contact the IT department.

        Best regards.
        """)           
        CHARSET = "UTF-8"
        # set your AWS region
        AWS_REGION="<SET YOUR AWS REGION>"
        ses_client = boto3.client('ses', region_name=AWS_REGION)
        # verify if the configuration set is created, if not then create it
        try:
            response = ses_client.create_configuration_set(
                ConfigurationSet={
                    'Name': 'my-config-set'
                }
            )   
        except Exception as e:
            print('Configuration set exists:' + e.response['Error']['Message'])
        else:
            print(f'Configuration set creation error !!! Please check your configuration set')
        # send email
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
                ConfigurationSetName='my-config-set',
            )
        except ClientError as e:
            print(f"Error sending email: {e.response['Error']['Message']}")
        else:
            print(f"Email sent! Message ID: {response['MessageId']}")

    def delete_user_items(user):
        """ function to delete all items linked to a user """
        try:
            # Delete access keys
            access_keys = iam_client.list_access_keys(UserName=user)
            for access_key in access_keys['AccessKeyMetadata']:
                iam_client.delete_access_key(UserName=user, AccessKeyId=access_key['AccessKeyId'])
            print(f"Access keys deleted for {user}")

            # Delete signing certificates
            certificates = iam_client.list_signing_certificates(UserName=user)
            for certificate in certificates['Certificates']:
                iam_client.delete_signing_certificate(UserName=user, CertificateId=certificate['CertificateId'])
            print(f"Signing certificates deleted for {user}")

            # Delete SSH public keys
            ssh_keys = iam_client.list_ssh_public_keys(UserName=user)
            for key in ssh_keys['SSHPublicKeys']:
                iam_client.delete_ssh_public_key(UserName=user, SSHPublicKeyId=key['SSHPublicKeyId'])
            print(f"SSH public keys deleted for {user}")

            # Delete service-specific credentials
            service_credentials = iam_client.list_service_specific_credentials(UserName=user)
            for credential in service_credentials['ServiceSpecificCredentials']:
                iam_client.delete_service_specific_credential(UserName=user, ServiceSpecificCredentialId=credential['ServiceSpecificCredentialId'])
            print(f"Service-specific credentials deleted for {user}")

            # Delete inline policies
            policies = iam_client.list_user_policies(UserName=user)
            for policy_name in policies['PolicyNames']:
                iam_client.delete_user_policy(UserName=user, PolicyName=policy_name)
            print(f"Inline policies deleted for {user}")

            # Detach managed policies
            attached_policies = iam_client.list_attached_user_policies(UserName=user)
            for policy in attached_policies['AttachedPolicies']:
                iam_client.detach_user_policy(UserName=user, PolicyArn=policy['PolicyArn'])
            print(f"User managed policies detached for {user}")

            # Remove user from groups
            user_groups = iam_client.list_groups_for_user(UserName=user)
            for group in user_groups['Groups']:
                iam_client.remove_user_from_group(UserName=user, GroupName=group['GroupName'])
            print(f"User removed from groups for {user}")

            # Delete mfa devices
            mfa_devices = iam_client.list_mfa_devices(UserName=user)
            for mfa_device in mfa_devices['MFADevices']:
                iam_client.delete_virtual_mfa_device(SerialNumber=mfa_device['SerialNumber'])
            print(f"MFA devices deleted for {user}")

            # Delete the password (login profile)
            iam_client.delete_login_profile(UserName=user)
            print(f"Password deleted for user: {user}")

        except ClientError as e:
            print(f"Error deleting user items for {user}: {e}")    


    # delete incorrect users
    if __name__ == '__main__':
        incorrect_users_list = list_incorrect_users()
        for user in incorrect_users_list:
            delete_user_items(user)
            iam_client.delete_user(UserName=user)
            users_deleted.append(user)
        send_mail(users_deleted)
