# This is a module from functions.py

# Create a function to display a welcome message
def  welcome():
  print('Hi !! Welcome to our python course')

# create a function greet() to display a hello message
def  greet():
  print('Hello everyone')

# create a function add_num to summarize two numbers
def add_num(a,b = 2):
  return a + b

# Define `divide()` with required arguments
def divide(a,b):
  return a / b

# Define `add_num()` function to accept a variable number of arguments
def add_num(*args):
  return sum(args)

# Define `add_num()` function to accept a variable number of arguments
def add_num(*args):
  total = 0
  for i in args:
          total += i
  return total

# create function to return the square of a number
def square(x):
  return x * x

# pass statement in a function
def myfunction():
  pass

