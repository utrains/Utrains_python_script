# Control flow and loops: solutions of exercises

1. Loot at the following code:
``` python
if x==y ………… k==z:
  print('Welcome to control flow exercises')
```
* Fill the dotted line to be able to print 'Welcome to control flow exercises' if x is equal to y, and k is equal to z.
``` python
if x==y and k==z:
  print('Welcome to control flow exercises')
```
* Fill the dotted line to be able to print 'Welcome to control flow exercises' if x is equal to y, or k is equal to z.
``` python
if x==y or k==z:
  print('Welcome to control flow exercises')
```
2. Find the error in the following code and correct it:
``` python
if 12 > 10:
print('twelve is greater than ten')
```
* This code will throw an error because statement of if condition is not **indented**. Let's correct it:
``` python
if 12 > 10:
  print('twelve is greater than ten')
```
3. Complete the following code to print  i as long as it is less than 10:

``` python
i=4
………… i < 10 …
  print(i)
  i+=1
```
The correct code is below:
``` python
i=4
while i < 10:
  print(i)
  i+=1
```
4. Complete the following code to stop the loop if i is 5.
``` python
i=1
while i < 10:
  print(i)
  if i == 5:
      ……………	
  i += 1
```
The correct code is beloow:
``` python
i=1
while i < 10:
  print(i)
  if i == 5:
      break	
  i += 1
```
Let’s have the list below:
``` python
courses=['linux','vagrant','docker','kubernetes', 'python']
```
5. Write a python script to show all items of the above list using for loop.
``` python
for course in courses:
  print(course)
```
6. Write a python script to show all items of the above list using while loop.
``` python
i=0
while i < len(courses):
  print(course)
```
7. Give the output of the following code:
``` python
for x in courses:
  if x=='docker':
     continue
  print(x)
```
This code will display all the elements before 'docker', then stop on it and display all the following elements. Let's see the output:
* **linux**
* **vagrant**
* **kubernetes**
* **python**

8. Give the output of the following code:

``` python
for x in courses:
  if x=='docker':
     break
  print(x)
```
This code will display all the elements before 'docker', then stop on it and exit from the for loop. Let's see the output:
* **linux**
* **vagrant**
