## The goal of this document is to manipulate the following built-in modules:
* OS module
* Sys module
* Math module
* Statistics module
* Random module

### The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.

``` python
import os
# get the current working directory
os.getcwd()

# create a new directory
os.mkdir('file path') # example for my side 'file path'='C:\\Users\\Reyel\\Utrains\\MyPythonProject'

# remove a specified directory
os.rmdir('file path') # example for my side 'file path'='C:\\Users\\Reyel\\Utrains\\MyPythonProject'
```
### The sys module provides functions and variables used to manipulate different parts of the Python runtime environment.

``` python
import sys
# check the largest integer a variable 
sys.maxsize

# display an environment variable that is a search path for all Python modules
sys.path

# display a string containing the version number of the current Python interpreter
sys.version
```
### The math module include trigonometric functions, representation functions, logarithmic functions, angle conversion functions, etc. wo mathematical constants are also defined in this module (pi and Euler's number (e) ).

``` python
import math
# get the value of pi and Euler's number
math.pi
math.e

# get a float number after raising e to the power of the given number.
math.exp(10) # the given number is 10

# get the square root of a given number 
math.sqrt(25)

# take two numbers and raises the first to the second
math.pow(5,2)
```
### The statistics module provides functions to mathematical statistics of numeric data.

``` python
import statistics
# calculate the arithmetic mean of the numbers in a list.
statistics.mean([1,8,10,6,4])

# get the middle value of numeric data in a list.
statistics.median([1,8,10,6,4])

# get the most common data point in the list.
statistics.mode([2,5,3,2,8,3,9,4,2,5,6])
```
### The random module is a built-in module to generate the pseudo-random variables. 

``` python
import random
# get a random float number between 0.0 to 1.0
random.random()

# get a random integer between two specified integers.
random.randint(1,20)

# randomly reorders the elements in a list.
numbers=[12,23,45,67,65,43]
random.shuffle(numbers)
print(numbers)
```
### The dir() function is used to list all the function names (or variable names) of a module in Python

``` python
import math
# Let’s list all functions names and variables names of math module
x= dir(math)
print(x)
```
