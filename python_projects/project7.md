## At work, part of the external audit showed that some of our S3 buckets are exposed and do not have encryption enabled and no bucket policy applied.

## Write a script that check all the S3 buckets and identifies which are not encrypted and have no bucket policy applied.

## The script is below:

``` python
import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

buckets_list = s3_client.list_buckets()

# get a list of bucket's names
buckets = []
for bucket in buckets_list['Buckets']:
    buckets.append(bucket['Name'])

def get_unencrypted_buckets():
    """ This function get a list of all s3 buckets without Encryption """
    _unencrypted_buckets=[]
    encryptionError='ServerSideEncryptionConfigurationNotFoundError'
    for bucket in buckets:
        try:
            # bucket has encryption enable
            _bucket_enc_response = s3_client.get_bucket_encryption(Bucket=bucket) 
            rules = _bucket_enc_response['ServerSideEncryptionConfiguration']['Rules']
            print(f"Bucket: {bucket}, Encryption: {rules}")
        except ClientError as e:
            if e.response['Error']['Code'] == encryptionError: # unencrypted bucket error
                print(f"Bucket: {bucket}, no server-side encryption")
                _unencrypted_buckets.append(bucket) # add unencrypted bucket in a list
            else: # any other type of error
                print(f"Bucket: {bucket}, unexpected error for encryption check: {e}")
    return _unencrypted_buckets

def get_nopolicy_buckets():
    """ This function get a list of all s3 buckets without policy"""
    _no_policy_buckets=[]
    policyError= 'NoSuchBucketPolicy'
    for bucket in buckets:
        try:
            # bucket has policy
            policy_status=s3_client.get_bucket_policy_status(Bucket=bucket)
            print(f"Bucket: {bucket}, policy: {policy_status}")
        except ClientError as e:
            if e.response['Error']['Code'] == policyError: # no policy bucket error
                print(f"Bucket: {bucket}, has no policy attached")
                _no_policy_buckets.append(bucket) # add no policy bucket in a list
            else:# any other type of error
                print(f"Bucket: {bucket}, unexpected error for policy check: {e}")
    return _no_policy_buckets

unencrypted_buckets= get_unencrypted_buckets()
nopolicy_buckets= get_nopolicy_buckets()

print("\n ############# List of buckets with no encryption: ########### \n")
if unencrypted_buckets:
    for bucket_name in unencrypted_buckets:
        print(f"\t \t Bucket: {bucket_name} \n")
else:
    print(f"\t \t All Buckets have encryption enable \n")

print("\n ############# List of buckets without policy: ########### \n")

if nopolicy_buckets:
    for bucket_name in nopolicy_buckets:
        print(f"\t \t Bucket: {bucket_name} \n")
else:
    print(f"\t \t All Buckets have policy \n")
    
```
