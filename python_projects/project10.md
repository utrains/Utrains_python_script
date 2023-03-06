## For security purposes, all users must rotate their access key every 90 days.

### Write a script that will check all users' access keys and deactivate the ones that are non-compliant. Also, this script should send a warning email to users to rotate their access keys after 85 days. All access keys should automatically be deactivated after 90 days, which can be associated with a Jenkins job to periodically check the users access keys.

### Attach policies for IAM and SES to the role of your lambda function in AWS.

## The script is below:

``` python
import boto3, datetime
from datetime import date
from botocore.exceptions import ClientError

iam = boto3.client('iam')

def send_mail(email_list):
    # emails in email_list must be verified by AWS SES
    RECIPIENTS = email_list
    # set your verified email address from AWS SES
    SENDER = "<SET YOUR SENDER EMAIL>"
    SUBJECT = "WARNING!!! IAM Access Key Rotation"
    BODY_TEXT = ("Your IAM Access Key need to be rotated immediately as it is 3 months or older.\n" 
                "If not, it will be deactivated shortly.")           
    CHARSET = "UTF-8"
    # set your AWS REGION
    AWS_REGION="<AWS_REGION>"
    ses_client = boto3.client('ses', region_name=AWS_REGION)
    try:
        response = ses_client.send_email(
            Destination={
                'ToAddresses': RECIPIENTS,
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

for user in iam.list_users()['Users']: # check for all iam users 
    # get a list of access keys for a user
    userKeys = iam.list_access_keys(UserName=user['UserName'])
    for keyValue in userKeys['AccessKeyMetadata']:
        # check if access key is active
        if keyValue['Status'] == 'Active':
            currentdate = date.today()
            active_days = currentdate - keyValue['CreateDate'].date()
            if (active_days >= datetime.timedelta(days=85)) and (active_days <= datetime.timedelta(days=90)):
                userTags = iam.list_user_tags(UserName=keyValue['UserName'])
                # get the list of email from tags as key:value
                email_tags = list(filter(lambda tag: tag['Key'] == 'email', userTags['Tags']))
                email_list = []
                # make a list of email from tags 
                for email_tag in email_tags:
                    email = email_tag['Value']
                    email_list.append(email)
                    print(email)
                # to remove duplicated emails
                email_unique = list(set(email_list))
                if len(email_unique) >= 1:
                    # send mail to email from tag
                    send_mail(email_unique)
                else:
                    print('There is no email address in the tags')
            elif active_days > datetime.timedelta(days=90):
                # deactivate keys 
                iam.update_access_key(UserName=keyValue['UserName'], AccessKeyId=keyValue['AccessKeyId'], Status='Inactive')
                print(f"Access keys of {keyValue['UserName']} have been deleted")
            else:
                pass```
