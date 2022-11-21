import boto3

AWS_REGION="<SET YOUR REGION>"

ec2_client=boto3.client("ec2",region_name=AWS_REGION)

regions=[]
for each_region_info in  ec2_client.describe_regions().get('Regions'):
  regions.append( each_region_info.get('RegionName'))


print(f"All regions for ec2 service are: \n {regions}")
