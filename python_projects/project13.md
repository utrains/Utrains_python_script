## At work, we usually create manually repositories in Github. There is a ticket assigned to you to automatically create, update and list repositories from github using python and requests module.

### The script is below
```python

import requests
import json

# Define the API endpoint
url = "https://api.github.com"

# Define the headers to include the authorization token
headers = {
    "Authorization": "<YOUR_AUTH_TOKEN>"
}

# Define a function to get a list of repositories for a user
def get_repos(username):
    endpoint = f"{url}/users/{username}/repos"
    response = requests.get(endpoint, headers=headers)
    repos = json.loads(response.text)
    return repos

# Define a function to create a repository for a user
def create_repo(username, repo_name):
    endpoint = f"{url}/user/repos"
    data = {
        "name": repo_name,
        "private": False
    }
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
    else:
        print(f"Error creating repository '{repo_name}'")

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
        print(f"Error updating repository '{repo_name}'")

# Define a function to delete a repository for a user
def delete_repo(username, repo_name):
    endpoint = f"{url}/repos/{username}/{repo_name}"
    response = requests.delete(endpoint, headers=headers)
    if response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully!")
    else:
        print(f"Error deleting repository '{repo_name}'")

# Test the functions
repos = get_repos("<YOUR_USERNAME>")
print(repos)



```
