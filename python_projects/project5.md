## The dev team is using a script to inventory instance infos from aws using the boto3 module. (the script is querying all instances with tag {environment: dev} this value is hard coded in the script. please modify the script so the qa team and eventually the subsequent team can use it to do the same.

```python
#!/usr/bin/python
'''
This script starts all instances with a specific tag.
'''

import boto3

#ec2_client=boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

def instances_find(name, value):
    '''
    Finds instance id's based on tags.
    Returns a list of instances found.
    '''
    list_instances = []
    # filter based on tags
    filters =[
        {
        'Name': name,
        'Values': [
            value,
            ]
        },
    ]
    instances = ec2_resource.instances.filter(Filters=filters)
    
    
    for instance in instances:
        
        # for each instance, append to list
        list_instances.append(instance)
        #list_instances.append(instance.describe_instances())

    return list_instances

def show_instances(instances):
    header = "instance.id\t\t instance_type\t\t instance_image.id"
    print(header)
    for instance in instances:
        instance_details = f"{instance.id}\t {instance.instance_type} \t\t{instance.image_id}"
        print(instance_details)


# def instances_start(list):
    #'''
    #Starts instances defined in the list.
    #'''
    # ec2_client.start_instances(InstanceIds=list)

# enter tag name and value
tag_name = 'tag:environment'
tag_value = 'dev'


# find instances
ec2_list = instances_find(tag_name, tag_value)


#show instances
show_instances(ec2_list)

```
