## The script in project8 is running locally, Configure it to run periodically (every week)  with lambda function and email the security team with any findings.

## The script is below:

### Attach policies for S3 and SES to the role of your lambda function in AWS.

``` python
import boto3
import json
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    s3_client = boto3.client('s3')

    buckets_list = s3_client.list_buckets()

    # get a list of bucket's names
    buckets = []
    for bucket in buckets_list['Buckets']:
        buckets.append(bucket['Name'])
    AWS_REGION='ap-south-1'
    def get_EncryptedFixed_buckets():
        """ This function find all s3 buckets without Encryption and fixed them, 
        then return the list of fixed buckets """
        unencrypted_buckets_fixed=[]
        encryptionError='ServerSideEncryptionConfigurationNotFoundError'
        for bucket in buckets:
            try:
                _bucket_enc_response = s3_client.get_bucket_encryption(Bucket=bucket)
                rules = _bucket_enc_response['ServerSideEncryptionConfiguration']['Rules']
                print(f"Bucket: {bucket}, Encryption: {rules}")
            except ClientError as e:
                if e.response['Error']['Code'] == encryptionError:
                    print(f"Bucket: {bucket}, no server-side encryption")
                    # put encryption on the bucket
                    s3_client.put_bucket_encryption(
                        Bucket= bucket,
                        ServerSideEncryptionConfiguration={
                            'Rules': [
                                {'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'AES256'}},
                            ]
                        }
                    )
                    print(f"Encryption fixed on {bucket}")
                    unencrypted_buckets_fixed.append(bucket)
                else:
                    print(f"Bucket: {bucket}, unexpected error for encryption check: {e}")
        return unencrypted_buckets_fixed


    def set_bucket_policy(bucket_name):
        """ This function is used to attach a policy to a bucket"""
        ### change the IAM_USER_ARN in the bucket_policy
        bucket_policy={
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "VisualEditor0",
                    "Effect": "Allow",
                    "Action": "s3:*",
                    "Resource": f"arn:aws:s3:::{bucket_name}/*",
                    "Principal": {
                        "AWS": [
                            "<SET YOUR IAM_USER_ARN>",
                        ]
                    },
                }
            ]
        }
        bucket_policy=json.dumps(bucket_policy)
        response = s3_client.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
        return response

    def get_NoPolicyFixed_buckets():
        """ This function find all s3 buckets with no policy and attach policy to them, 
        then return the list of fixed buckets """
        _no_policy_buckets_fixed=[]
        policyError= 'NoSuchBucketPolicy'
        for bucket in buckets:
            try:
                policy_status=s3_client.get_bucket_policy_status(Bucket=bucket)
                print(f"Bucket: {bucket}, policy: {policy_status}")
            except ClientError as e:
                if e.response['Error']['Code'] == policyError:
                    print(f"Bucket: {bucket}, has no policy attached")
                    try:
                        attached_policy= set_bucket_policy(bucket)
                        print(attached_policy)
                        _no_policy_buckets_fixed.append(bucket)
                        print(f"Policy attached to {bucket}")  
                    except ClientError as e:
                        print(f"no policy attached, {e}")
                else:
                    print(f"Bucket: {bucket}, unexpected error for policy check: {e}")
        return _no_policy_buckets_fixed

    encrypted_buckets= get_EncryptedFixed_buckets()
    fixed_policy_buckets= get_NoPolicyFixed_buckets()
    buckets_fixed=list(set(encrypted_buckets+fixed_policy_buckets))

    def send_mail():
        # set a verified email address of security team
        RECIPIENT = ["<SET A VERIFIED EMAIL OF SECURITY TEAM>"]
        # set your verified sender email address
        SENDER = "<SET A VERIFIED SENDER EMAIL>"
        SUBJECT = "Encryption and Policy fixed on S3 buckets"
        BODY_TEXT = (f"""
        Hello Security team, 
        This mail is to you notify that, we have applied encryption and policy on all the buckets 
        in the list below: 
        {buckets_fixed}""")           
        CHARSET = "UTF-8"
        ses_client = boto3.client('ses')
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
            
    # send mail if buckets_fixed is not empty
    if buckets_fixed:
        send_mail()
    else:
        print("All the Buckets are good !!!")  
 ```
