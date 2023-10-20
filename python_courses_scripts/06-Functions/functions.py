# This python script help you to manipulate functions in python

# Create a function to display a welcome message
def  welcome():
  print('Hi !! Welcome to our python course')

# create a function greet() to display a hello message
def  greet():
  print('Hello everyone')
greet() # to call the function greet

# create a function add_num to summarize two numbers
def add_num(a,b = 2):
  return a + b
# Call `add_num()` with only `a` parameter and display the return value
add1= add_num(a=1)
print(add1)
# Call `add_num()` with `a` and `b` parameters and display the return value
add2= add_num(a=1, b=3)
print(add2)

# Define `divide()` with required arguments
def divide(a,b):
  return a / b
# call divide()' with required arguments and display the return value
quotient= divide(8, 10)
print(quotient)

# Call `divide()` function with keyword arguments
quotient1=divide(a=2, b=5)
print('quotient1 value is: ', quotient1)
# Call `divide()` function with keyword arguments and change order
quotient2=divide(b=5, a=2)
print('quotient2 value is: ', quotient2)

# Define `add_num()` function to accept a variable number of arguments
def add_num(*args):
  return sum(args)
# Calculate the sum
sum_args=add_num(2,4,6,8)
print('the sum of arguments is: ', sum_args)

# Define `add_num()` function to accept a variable number of arguments
def add_num(*args):
  total = 0
  for i in args:
          total += i
  return total
# Calculate the sum  
sum_args=add_num(2,4,6,8)
print('the sum of arguments is: ', sum_args)

# create function to return the square of a number
def square(x):
  return x * x

# pass statement in a function
def myfunction():
  pass

