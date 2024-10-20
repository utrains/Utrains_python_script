## To maintain a secure and well-organized AWS environment, we need to develop a Python script to automate the cleanup of IAM roles in our AWS environment. The goal is to identify and delete IAM roles that are older than a specified threshold (100 days) using the Boto3 library. This automation will help maintain a secure, efficient, and organized AWS account by regularly removing outdated or unused roles.

## The script will become part of our routine maintenance, running on a schedule to automate IAM role cleanup and keep our AWS environment in optimal condition.

## The script should:

#### 1. Retrieve all IAM roles in the AWS account.
#### 2. Determine the age of each role based on its creation date.
#### 3. Delete roles that are older than the configured threshold (100 days).


### The proposed solution is below:

``` python


import boto3
import datetime
from botocore.exceptions import ClientError

# Function to delete the IAM role
def delete_iam_role(role_name):
    # create an iam boto3 client
    client = boto3.client('iam')
    try:
        # delete the role by its name
        response = client.delete_role(RoleName=role_name)
        print(f"Role {role_name} deleted successfully")
    except ClientError as e:
        # display the error message if the role can't be deleted
        print(f"Error deleting role {role_name}:{e.response['Error']['Message']}")
    
    

# Function to get the age of the role

def get_role_age(role_name):
    # Create an IAM boto3 client
    client = boto3.client('iam')
    try:
        # Retrieve role information
        response = client.get_role(RoleName=role_name)
    except ClientError as e:
        # Display an error message if role details can't be retrieved
        print(f"Error retrieving role {role_name}:{e.response['Error']['Message']}")
        return None  # Return None if there's an error

    # Get the role creation date and current date    
    role_creation_date = response['Role']['CreateDate']
    current_date = datetime.datetime.now(datetime.timezone.utc)
    # compute the role's age
    age = (current_date - role_creation_date).days
    
    return age

# Function to get the list of roles
def get_role_list():
    # Create an IAM boto3 client
    client = boto3.client('iam')
    try:
        # List all roles
        response = client.list_roles()
    except ClientError as e:
        # Display an error message if roles can't be listed
        print(f"Error listing roles: {e.response['Error']['Message']}")
        return []  # Return an empty list if there's an error
    
    # Extract role names
    role_list = [role['RoleName'] for role in response['Roles']]
    return role_list
    
def main():
    """
    Main function to check IAM roles and delete those older than 100 days.
    """
    # Get the list of all roles
    roles = get_role_list()
    # Iterate over each role
    for role in roles:
        # Get the age of the role
        age = get_role_age(role)
        # If age is greater than 100 days, delete the role
        if age is not None and age > 100:
            delete_iam_role(role)

if __name__ == '__main__':
    main()