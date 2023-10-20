import boto3
import json

# Interacting with Boto3 and Amazon Simple Queue Services (SQS)
# create a new SQS queue
def create_queue(queue_name):
    sqs_client = boto3.client("sqs", region_name="ca-central-1")
    response = sqs_client.create_queue(
        QueueName=queue_name,
        Attributes={
            "DelaySeconds": "5",
            "VisibilityTimeout": "60",
        }
    )
    print(response)

#create_queue("my-new-queue")

# get the url of the SQS queue
def get_queue_url(queue_name):
    sqs_client = boto3.client("sqs", region_name="ca-central-1")
    response = sqs_client.get_queue_url(
        QueueName=queue_name,
    )
    return response["QueueUrl"]

#get_queue_url("my-new-queue")

# send a message to the SQS queue

def send_message(queue_url):
    sqs_client = boto3.client("sqs", region_name="ca-central-1")

    message = {"key": "value"}
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message)
    )
    print(response)
#send_message("https://ca-central-1.queue.amazonaws.com/076892551558/my-new-queue")

# receive a message from a sqs queue
def receive_message(queue_url):
    sqs_client = boto3.client("sqs", region_name="ca-central-1")
    response = sqs_client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=10,
    )
    
    print(f"Number of messages received: {len(response.get('Messages', []))}")
    for message in response.get("Messages", []):
        message_body = message["Body"]
        print(f"Message body: {json.loads(message_body)}")
        print(f"Receipt Handle: {message['ReceiptHandle']}")
    return response
#receive_message("https://ca-central-1.queue.amazonaws.com/076892551558/my-new-queue")

# delete a message from the SQS queue
def delete_message(queue_url):
    message= receive_message()["Messages"][0]
    receipt_handle= message['ReceiptHandle']
    sqs_client = boto3.client("sqs", region_name="ca-central-1")
    response = sqs_client.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle,
    )
    print(response)
#delete_message("https://ca-central-1.queue.amazonaws.com/076892551558/estephe-new-queue")

# change DelaySeconds and VisibilityTimeout attributes of my-new-queue
def change_queue_attributes(queue_url):
    sqs_client = boto3.client("sqs", region_name="ca-central-1")
    response = sqs_client.set_queue_attributes(
        QueueUrl=queue_url,
        Attributes={
            "DelaySeconds": "10",
            "VisibilityTimeout": "300",
        }
    )
    print(response)
#change_queue_attributes("https://ca-central-1.queue.amazonaws.com/076892551558/my-new-queue")

# delete all messages from my-new-queue
def purge_queue(queue_url):
    sqs_client = boto3.client("sqs", region_name="ca-central-1")
    response = sqs_client.purge_queue(
        QueueUrl=queue_url,
    )
    print(response)
#purge_queue("https://ca-central-1.queue.amazonaws.com/076892551558/my-new-queue")

