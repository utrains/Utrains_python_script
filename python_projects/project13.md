## At work, we usually create manually repositories in Github. There is a ticket assigned to you to automatically create, update and list repositories from github using python and requests module.

### The script is below
```python

import requests
import json

# Define the API endpoint
url = "https://api.github.com"

# Define the headers to include the authorization token
# Link to generate your auth token:
# https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic
token= "<YOUR_AUTH_TOKEN>"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Define a function to get a list of repositories for a user
def get_repos(username):
    endpoint = f"{url}/users/{username}/repos"
    response = requests.get(endpoint, headers=headers)
    if response.status_code == 200:
        repos = response.json()
        print("\n ############# List of repositories: ########### \n")
        for repo in repos:
            print(f"repo_name:{repo['name']}, repo_url: {repo['html_url']}")
            print("\n ########################################### \n")

    else:
        print(f"Error getting repositories: {response.status_code}")


# Define a function to create a repository for a user
def create_repo(repo_name):
    endpoint = f"{url}/user/repos"
    data = {
        "name": repo_name,
        "private": False,
    }
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
    else:
        print(f"Error creating repository '{repo_name}': {response.status_code}")

# Define a function to update a repository for a user
def update_repo(username, repo_name, description):
    endpoint = f"{url}/repos/{username}/{repo_name}"
    data = {
        "description": description
    }
    response = requests.patch(endpoint, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print(f"Repository '{repo_name}' updated successfully!")
    else:
        print(f"Error updating repository '{repo_name}': {response.status_code}")

# Define a function to delete a repository for a user
def delete_repo(username, repo_name):
    endpoint = f"{url}/repos/{username}/{repo_name}"
    response = requests.delete(endpoint, headers=headers)
    if response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully!")
    else:
        print(f"Error deleting repository '{repo_name}': {response.status_code}")

# Test the functions
if __name__ == "__main__":
    # Replace <YOUR_USERNAME> with your GitHub username
    username = "<YOUR_USERNAME>"
    
    # Get repositories
    get_repos(username)
        
    # Create a new repository
    repo_name = "test-repo-new"
    create_repo(repo_name)
    
    # Update the repository
    update_repo(username, repo_name, "Updated description")
    
    # Delete the repository
    delete_repo(username, repo_name)

```
