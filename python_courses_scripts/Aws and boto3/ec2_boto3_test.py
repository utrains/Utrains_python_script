import boto3

# Interacting with Boto3 and Amazon Elastic Compute Cloud (EC2)
# create an EC2 key pair
def create_key_pair():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.create_key_pair(KeyName="my-ec2-key-pair")   
    print(response)

#create_key_pair()

# create an EC2 instance
def create_instance():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    instances = ec2_client.run_instances(
        ImageId="ami-090fa75af13c156b4",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="my-ec2-key-pair"
    )
    print(f'Instance id: {instances["Instances"][0]["InstanceId"]}')

#create_instance()

# get a public key of an EC2 instance
def get_public_ip(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(f'public IP adress: {instance.get("PublicIpAddress")}')

#get_public_ip('i-0a20cf982109974f5')

# to list all running EC2 instances

def get_running_instances():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")
    print("instance.id\t\tinstance_type\tpublic IP address\tprivate IP address\n")
    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            public_ip = instance.get("PublicIpAddress")
            private_ip = instance.get("PrivateIpAddress")
            print(f"{instance_id}\t{instance_type}\t{public_ip}\t\t\t{private_ip}")

#get_running_instances()

# stop an EC2 instance we created.
def stop_instance(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(response)

#stop_instance('i-0a20cf982109974f5')

# terminate an EC2 instance
def terminate_instance(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)

#terminate_instance('i-0a20cf982109974f5')
