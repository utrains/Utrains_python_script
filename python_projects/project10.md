## For security purposes, all users must rotate their access key every 90 days.

### Write a script that will check all users' access keys and deactivate the ones that are non-compliant. Also, this script should send a warning email to users to rotate their access keys 85 days before the deactivation. All access keys should automatically be deactivated after 90 days, which can be associated with a Jenkins job to periodically check the users access keys.

## The script is below:

``` python
import boto3, datetime
from datetime import date
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    iam = boto3.client('iam')
    email_list = []

    def send_mail(email_list):
        RECIPIENTS = email_list
        # set your verified sender email address
        SENDER = "<SET YOUR SENDER EMAIL>"
        SUBJECT = "WARNING!!! IAM Access Key Rotation"
        BODY_TEXT = ("Your IAM Access Key need to be rotated immediately as it is 3 months or older.\n" 
                    "If not, it will be deactivated shortly.")           
        CHARSET = "UTF-8"
        ses_client = boto3.client('ses')
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

    for userlist in iam.list_users()['Users']:
        userKeys = iam.list_access_keys(UserName=userlist['UserName'])
        for keyValue in userKeys['AccessKeyMetadata']:
            if keyValue['Status'] == 'Active':
                currentdate = date.today()
                active_days = currentdate - \
                    keyValue['CreateDate'].date()
                if (active_days >= datetime.timedelta(days=85)) and (active_days <= datetime.timedelta(days=90)):
                    userTags = iam.list_user_tags(
                        UserName=keyValue['UserName'])
                    email_tag = list(filter(lambda tag: tag['Key'] == 'email', userTags['Tags']))
                    if(len(email_tag) == 1):
                        email = email_tag[0]['Value']
                        email_list.append(email)
                        print(email)
                    email_unique = list(set(email_list))
                    send_mail(email_unique)
                elif active_days > datetime.timedelta(days=90):
                    iam.update_access_key(UserName=keyValue['UserName'], AccessKeyId=keyValue['AccessKeyId'], Status='Inactive',)
                   
```
