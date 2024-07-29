## EBS Snapshots are a copy of your data at a certain time, and can be used to enable disaster recovery, migrate data across regions and accounts, and improve backup compliance. 

## Write a script that can automate AWS EBS snapshots and notify the admin via email.

### Note: This script needs to be executed twice: the first you will confirm the subscription email, and the second time to send the notification.

```python
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from datetime import datetime

def create_snapshots_and_notify():

    AWS_REGION = 'us-esat-1'
    ec2_client = boto3.client('ec2', region_name=AWS_REGION)

    snapshots = []

    try:
        # Create snapshots for available volumes
        response = ec2_client.describe_volumes()
        for volume in response['Volumes']:
            volume_id = volume['VolumeId']
            description = f'Snapshot of {volume_id} on {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
            
            snapshot = ec2_client.create_snapshot(VolumeId=volume_id, Description=description)
            snapshots.append(snapshot['SnapshotId'])
            print(f"Snapshot created successfully for volume {volume_id}")
            

        # Create a notification topic
        topic_name = 'EBS-Snapshot-notification'
        sns_client = boto3.client("sns", region_name=AWS_REGION)
        topic = sns_client.create_topic(Name=topic_name)
        topic_arn = topic['TopicArn']

        # Subscribe an email to the topic
        # Email needs to be manually confirmed first
        protocol = 'email'
        email = '<SET YOUR ADMIN EMAIL HERE>'

        # Check if the subscription already exists
        subscriptions = sns_client.list_subscriptions_by_topic(TopicArn=topic_arn)['Subscriptions']
        email_exists = any(sub['Endpoint'] == email for sub in subscriptions)

        if not email_exists:
            sns_client.subscribe(
                TopicArn=topic_arn,
                Protocol=protocol,
                Endpoint=email,
                ReturnSubscriptionArn=True
            )

        # Publish a message to the topic via email
        if snapshots:
            message = f"""We successfully created snapshots of your available volumes.
            Here is the list of their IDs: {', '.join(snapshots)}"""
            subject = 'EBS Snapshots'
            response = sns_client.publish(
                TopicArn=topic_arn,
                Message=message,
                Subject=subject,
            )
            message_id = response['MessageId']
            print(f'Message published to topic {topic_arn} with message ID: {message_id}')
        else:
            print('No snapshots were created.')

    except (NoCredentialsError, PartialCredentialsError):
        print("Error: AWS credentials not found or incomplete.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    create_snapshots_and_notify()

```
