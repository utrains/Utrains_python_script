import boto3
import json

# Interacting with Boto3 and Amazon Simple Queue Services (SQS)
# create a new SQS queue
def create_queue():
    sqs_client = boto3.client("sqs", region_name="ca-central-1")
    response = sqs_client.create_queue(
        QueueName="my-new-queue",
        Attributes={
            "DelaySeconds": "5",
            "VisibilityTimeout": "60",
        }
    )
    print(response)

#create_queue()

# get the url of the SQS queue
def get_queue_url():
    sqs_client = boto3.client("sqs", region_name="ca-central-1")
    response = sqs_client.get_queue_url(
        QueueName="my-new-queue",
    )
    return response["QueueUrl"]

#get_queue_url()

# send a message to the SQS queue

def send_message():
    sqs_client = boto3.client("sqs", region_name="ca-central-1")

    message = {"key": "value"}
    response = sqs_client.send_message(
        QueueUrl="https://ca-central-1.queue.amazonaws.com/076892551558/my-new-queue",
        MessageBody=json.dumps(message)
    )
    print(response)
#send_message()

# receive a message from a sqs queue
def receive_message():
    sqs_client = boto3.client("sqs", region_name="ca-central-1")
    response = sqs_client.receive_message(
        QueueUrl="https://ca-central-1.queue.amazonaws.com/076892551558/my-new-queue",
        MaxNumberOfMessages=1,
        WaitTimeSeconds=10,
    )
    
    print(f"Number of messages received: {len(response.get('Messages', []))}")
    for message in response.get("Messages", []):
        message_body = message["Body"]
        print(f"Message body: {json.loads(message_body)}")
        print(f"Receipt Handle: {message['ReceiptHandle']}")
    return response
#receive_message()

# delete a message from the SQS queue
def delete_message():
    message= receive_message()["Messages"][0]
    receipt_handle= message['ReceiptHandle']
    sqs_client = boto3.client("sqs", region_name="ca-central-1")
    response = sqs_client.delete_message(
        QueueUrl="https://ca-central-1.queue.amazonaws.com/076892551558/estephe-new-queue",
        ReceiptHandle=receipt_handle,
    )
    print(response)
#delete_message()

# change DelaySeconds and VisibilityTimeout attributes of my-new-queue
def change_queue_attributes():
    sqs_client = boto3.client("sqs", region_name="ca-central-1")
    response = sqs_client.set_queue_attributes(
        QueueUrl="https://ca-central-1.queue.amazonaws.com/076892551558/my-new-queue",
        Attributes={
            "DelaySeconds": "10",
            "VisibilityTimeout": "300",
        }
    )
    print(response)
#change_queue_attributes()

# delete all messages from my-new-queue
def purge_queue():
    sqs_client = boto3.client("sqs", region_name="ca-central-1")
    response = sqs_client.purge_queue(
        QueueUrl="https://ca-central-1.queue.amazonaws.com/076892551558/my-new-queue",
    )
    print(response)
#purge_queue()

