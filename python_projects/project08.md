## After finding the s3 buckets that don't have encryption enabled and no bucket policy applied based on project7's script, modify that to fix them accordingly.


## The script is below:

``` python

import boto3
import json
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

buckets_list = s3_client.list_buckets()


# get a list of bucket's names
buckets = []
for bucket in buckets_list['Buckets']:
    buckets.append(bucket['Name'])

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
                        "<IAM_USER_ARN>",
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

print("\n ############# List of buckets with no encryption fixed: ########### \n")
if encrypted_buckets:
    for bucket_name in encrypted_buckets:
        print(f"\t \t Bucket: {bucket_name} \n")
else:
    print(f"\t \t All Buckets are  encrypted \n")

print("\n ############# List of buckets without policy fixed: ########### \n")

if fixed_policy_buckets:
    for bucket_name in fixed_policy_buckets:
        print(f"\t \t Bucket: {bucket_name} \n")
else:
    print(f"\t \t All Buckets have policy \n")
    
```
