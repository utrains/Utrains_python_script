## EBS Snapshots are a copy of your data at a certain time, and can be used to enable disaster recovery, migrate data across regions and accounts, and improve backup compliance. 

## Write a script that can automate AWS EBS snapshots and notify the admin via email.

### Note: This script needs to be executed twice: the first you will confirm the subscription email, and the second time to send the notification.

```python
import boto3

ec2_resource = boto3.resource('ec2')

filter_vol= [
    {
        'Name':'status', 
        'Values': ['available']
    }
]
snapshots=[]

# Create snapshots for available volumes
for volume in ec2_resource.volumes.filter(Filters=filter_vol):
    snapshot=volume.create_snapshot(Description='Snapshot created via script')
    snapshots.append(snapshot.snapshot_id)
    print(f"Snapshot created successfully for volume {volume.id}")

# Create a notification topic
AWS_REGION='us-east-1'
topic_name='EBS-Snapshot-notification'
sns_client = boto3.client("sns", region_name=AWS_REGION)
topic = sns_client.create_topic(Name=topic_name)
topic_arn=topic['TopicArn']

# Subscribe an email to the topic
# email need to be manually confirmed first

protocol='email'
email='<SET YOUR ADMIN EMAIL HERE>'

email_sub= sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol=protocol, 
    Endpoint=email, 
    ReturnSubscriptionArn=True
)

# publish a message to a topic via email

if snapshots:
	message= f"""We sucessfully created snapshots of your available volumes. 
	Here is the list of their IDs: {snapshots}"""
	subject='EBS Snapshots'
	response= sns_client.publish(
		TopicArn=topic_arn,
		Message=message,
		Subject=subject,
	)
	message_id=response['MessageId']
	print(f'Message published to topic {topic_arn} with message Id: {message_id}')
```
