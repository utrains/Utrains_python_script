1. Inside the below function, write a code to display the first parameter.
``` python
def my_function1(first_name, last_name):
  ..................
```
The correct code is below:

``` python
def my_function1(first_name, last_name):
  print(first_name)
  print(last_name)
```
2. Complete the code by the command to let the function return the x parameter + 18

``` python
def my_function2(x):
  ...............
```
The correct code is below:

``` python
def my_function2(x):
  return x+18
```
3. Write a Python function to summarize all the numbers of a list.

``` python
def summarize(list):
  sum=0
  for x in list:
    sum +=x
  return sum
```
4. If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, complete the following code with that prefix:

``` python
def my_function3(...kids):
  print("The youngest child is " + kids[4])
```
The correct code is below:
``` python
def my_function3(*kids):
  print("The youngest child is " + kids[4])
```
5. Write a Python function called max_two that return the maximum of two numbers.

``` python
def max_two( x, y ):
  if x > y:
      return x
  else
      return y
```
6. Write a Python function called max_three based on max_two function that return the maximum of three numbers.

``` python
def max_three(x, y, z):
    return max_of_two( x, max_two( y, z ) )
```
