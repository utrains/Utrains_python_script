#!/bin/python
import boto3

AWS_REGION="<SET YOUR REGION>"
ec2_client=boto3.client("ec2", region_name=AWS_REGION)
list_volumes_ids=[]

filter_avail={'Name':'status', 'Values': ['available']}
# get list of available Volumes Ids
paginator = ec2_client.get_paginator('describe_volumes')
for page in paginator.paginate(Filters=[filter_avail]):
    for each_vol in page['Volumes']:
        list_volumes_ids.append(each_vol['VolumeId'])

print(f"The volumes Ids are: {list_volumes_ids}")
# create a snapshot for each available volume
snapshots_ids=[]
for vol_id in list_volumes_ids:
    print(f"Taking snap of {vol_id}")
    response=ec2_client.create_snapshot( 
             Description="Taking snap with Lambda and cw",
             VolumeId=vol_id,
             TagSpecifications=[
                 {
                    'ResourceType':'snapshot',
                     'Tags': [
                         {
                            'Key': 'Delete-on',
                            'Value': '90'
                         }
                             ]
                 }
                ]
               )
    snapshots_ids.append(response.get('SnapshotId'))

print(f"The snapshots ids are: {snapshots_ids}")


waiter = ec2_client.get_waiter('snapshot_completed')
waiter.wait(SnapshotIds=snapshots_ids)

print(f"Succssfully created snapshots for the volumes of {list_volumes_ids}")
