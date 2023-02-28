#  Solutions of Python class exercises

## Exercise 1:  

Write a code that will take a string from user , and display how many characters are in that string.

### Solution:
```python
_string = input("Enter a string:  ")

resp = len(_string)

print(f"the lenght of your string is {resp}")
```

## Exercise 2:

Write a code that will take a string from user and if the string has less than 4 charactars, it should display "invalid entry"
and if the characters number in the string is more that 4 , it should display "valid entry".

### Solution:
```python
_entry = input("enter your string: ")

_string_len = len(_entry)

if _string_len < 4:
    print("invalid entry")
else:
    print("Valid entry")
```


## Exercise 3:

Write a code that will take email address as input and check if @ is in the email receive to tell the user if the email is valid or not.

### Solution:
```python
_email = input("Enter your email: ")

if '@'  in _email:
    print("valid email")
else:
    print("invalid email")
```

## Exercise 4:

Username and password of an application is admin. Write a code that takes two inputs from  user  username and password and tell the user "wrong username or password" if the username 
and password entered is not admin; and if it is admin and admin, it display "successfully login".

### Solution:
```python
_username = input("Enter your username: ")
_pass = input("Enter your password: ")

if _username == _pass == 'admin':
  print("You have successfully login")
else:
  print("Username or password wrong")
```

## Exercise 5:

Write a program to take user's zip code and check if the input data was a digit number with 5 digits. ( a good zip code has 5 digits)
if it is good , display "your entry is valid" if not , display "please enter a valid entry".

### Solution:
```python
_zip_code=input("Enter your zip code: ")

try:
    # check if the entry is a number
    _zip_code_cast=int(_zip_code)
    if len(_zip_code) == 5 :
        print("Your entry is valid")
    else:
        print("Please enter a valid entry")
except ValueError:
    print("ValueError !!! Please enter a zip code")
```

## Exercise 6:

Write a function that will take two integers and give the sum of those two int.

### Solution:
``` python

_integer1 = int(input("Enter your first integer: "))
_integer2 = int(input("Enter your second integer: "))

_sum = _integer1 + _integer2
  
print("The sum of  those two integers is: ", _sum)
```

## Exercise 7:

Write a program to inventory the linux system.

### Solution:
```python
import os

_numofCpu = os.cpu_count()
# display the number of cpu
print(_numofCpu)
# display a detailed report on the system's memory usage
os.system('free -m')
# list informations about all available or the specified block devices
os.system('lsblk')

```

## Consider you have these tickets at work. use help online from google, youtube to solve them:

## Exercise 8:

Write a python code that will enventory all iam users in aws.

### Solution:
```python
import boto3

_iam = boto3.client('iam')

users = _iam.list_users()

for i in users['Users']:
    print(i['UserName'])
```

## Exercise 9:

Write a python code that can be used to query infomation about all the jobs in jenkins. (jenkins needs to be migrated and we 
need a way to automate the jenkins server inventory.)

```python
import jenkins

# 'http://69.164.196.248:8080/' is the ip address of the jenkins server
_con = jenkins.Jenkins('http://69.164.196.248:8080/', username='utrains', password='school1')
jenkins_user = _con.get_whoami()
jenkins_version = _con.get_version()
job_number = _con.jobs_count()
jobs_name =_con.get_all_jobs()

print(f" Total number of jobs is: {job_number}")
print("\n Below is the list of all jobs in jenkins and thier url \n")
for i in jobs_name:
    
    print(i['name'] + "  " + i['url'])
```
## Exercise 10:

During deployment, there is a need to check an endpoint. If the return code is 200, then 
we know it is a success. This is done manually by typing the endpoint on the browser.
write a python code that will be integrated in the CD pipeline to check various endpoints automatically.
you can use https://www.wikipedia.org/ for positive testing https://www.wikipedia.org/class for negative testing of your code.

### Solution
``` python
import requests

response = requests.get('https://www.wikipedia.org/')

_code = response.status_code

if _code == 200:
    print("endpoint up and running")
else:
    print("End point down!!")
```
10-a) Change the script to request url from users.

### Solution
```python
import requests

_url = input("Enter the endpoint to be checked: ")

response = requests.get(_url)

_code = response.status_code

if _code == 200:
    print("endpoint up and running")
else:
    print("End point down!!")
```

10-b) If a user enter a malformed url, the code breaks your task is to catch that exception and tell the user that the url is not good.

### Solution
```python
import requests

_url = input("Enter your url here: ")

try:
    response = requests.get(_url)
    _code = response.status_code
    if _code == 200:
        print("endpoint up and running")
    else: 
        print("End point down!!")
except:
    print("Your Url is not good")
```

## Exercise 11:

In one of your projects, you need data from a specific team and they provided the data in xml format.
You need the data in csv or json format so you can easyly load it into bigquery (a big data service from google cloud)
Write a script that can be used to transform xml file into csv or json format. (you can use https://www.mockaroo.com/ to generate synthetique data for testing).

### Solution

Use the following link with your xml file from mockaroo as input:

https://github.com/utrains/Utrains_python_script/blob/main/python_projects/project5.md

