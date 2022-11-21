import boto3

# set your region
AWS_REGION="<SET YOUR REGION>"
ec2_resource=boto3.resource('ec2',region_name=AWS_REGION)

unused_untagged_volume_ids=[]

# check if unused and untagged volumes in the list of volumes
for each_vol in ec2_resource.volumes.all():
   if each_vol.state=="available" and each_vol.tags==None:
      print(each_vol.id, each_vol.state, each_vol.tags)
      unused_untagged_volume_ids.append(each_vol.id)

# Delete unused and untagged volumes
if unused_untagged_volume_ids:
    for each_vol_id in unused_untagged_volume_ids:
        ec2_volume=ec2_resource.Volume(each_vol_id)
        print (f"Deleting volume with id: {each_vol_id}")
        ec2_volume.delete()
        # remove the first id
        unused_untagged_volume_ids.pop(0)

    if not unused_untagged_volume_ids:
        print("Succsffuly deleted all your EBS volumes which are unused and untagged")
    else:
        print("There are still volumes not deleted")
else:
    print("No unused and untagged volumes detected")
