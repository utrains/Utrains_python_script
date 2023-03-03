import boto3

# Interacting with Boto3 and Amazon Simple Storage Service (S3)

# create Amazon s3 buckets with region name

def create_bucket(bucket_name, region):
    s3_client = boto3.client('s3', region_name=region)
    location = {'LocationConstraint': region}
    response=s3_client.create_bucket(Bucket=bucket_name,
                            CreateBucketConfiguration=location)
    print(response)

#create_bucket("first-utrains-bucket","ca-central-1")

# Retrieve the list of existing buckets
def list_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
                        
#list_buckets()

# Upload a file in the s3 bucket
def upload_file(file_name, bucket_name, key):
    s3_client = boto3.client('s3')
    s3_client.upload_file(file_name, bucket_name, key)

#upload_file('./test.txt', 'first-utrains-bucket', 'test.txt')

# download a file from a s3 bucket
def download_file(bucket_name, key, file_name):
    s3_client = boto3.client('s3')
    s3_client.download_file(bucket_name,key,file_name)

#download_file('first-utrains-bucket', 'test.txt', 'downloaded_test.txt')

# get the access control list of the specified bucket
def get_bucket_acl(bucket_name):
    s3_client = boto3.client('s3')
    result = s3_client.get_bucket_acl(Bucket=bucket_name)
    print(result)

#get_bucket_acl('first-utrains-bucket')

# delete an Amazon s3 bcuket

def delete_bucket(bucket_name):
    s3_client = boto3.client('s3', region_name="us-east-1")
    print("Before deleting the bucket we need to check if it's empty. Cheking ...")
    objects = s3_client.list_objects_v2(Bucket=bucket_name)
    fileCount = objects['KeyCount']

    if fileCount==0:
        response = s3_client.delete_bucket(Bucket=bucket_name)
        print("{} has been deleted successfully !!!".format(bucket_name))
        print(response)
    else:
        print("{} is not empty {} objects present".format(bucket_name,fileCount))
        print("Please make sure S3 bucket is empty before deleting it !!!")

#delete_bucket('first-utrains-bucket')
