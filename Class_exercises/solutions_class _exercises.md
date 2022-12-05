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
_username = input("Enter your username: ")
_pass = input("Enter your password: ")

if _username == _pass == 'admin':
  print("You have successfully login")
else:
  print("Username or password wrong")
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

## Consider you have these tickets at work. use help online from google, youtube to solve them:

## Exercise 8:

Write a python code that will enventory all iam users in aws.

## Exercise 9:

Write a python code that can be used to query infomation about all the jobs in jenkins. (jenkins needs to be migrated and we 
need a way to automate the jenkins server inventory.)

## Exercise 10:

During deployment, there is a need to check an end point. if the return code is 200, then 
we know it is a success. This is done manually by typing the endpoint on the browser.
write a python code that will be integrated in the CD pipeline to check various endpoints automatically.
you can use https://www.wikipedia.org/ for positive testing https://www.wikipedia.org/class for negative testing of your code.

10-a) change the script to request url from users.

10-b) If a user enter a malformed url, the code breaks your task is to catch that exception and tell the user that the url is not good.

## Exercise 11:

In one of your projects, you need data from a specific team and they provided the data in xml format.
you need the data in csv or json format so you can easyly load it into bigquery ( a big data service from google cloud)
Write a script that can be used to transform xml file into csv or json format. (you can use https://www.mockaroo.com/ to generate synthetique data for texting)


