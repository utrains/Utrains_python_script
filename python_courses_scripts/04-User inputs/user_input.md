## Up until now, our programs were static. The value of variables was defined or hard coded into the source code.

### To allow flexibility, we might want to take some inputs from the user. In Python, we have the input() function to allow this. 

### For example, let’s ask for user age and display it.
``` python
age= input("What's your age ?") # Enter your age then type ENTER
print(age)
```
### Whatever you enter as input, the input function converts it into a string.

### So, to take the input in the form of int you need to use int() along with the input function.

``` python
num=int(input('Enter a number: '))
sum= num+10
print(type(num))
print(sum)
```
### Let’s take the the input as a float:

``` python
num=float(input('Enter a number: '))
sum= num+10
print(type(num))
print(sum)
```
### Let’s take a list as input with the input() function. list() converts every type of entry (int, float and string) into a list of its elements.

``` python
# Taking input from the user as list
input_list=list(input('Enter a number: '))
print(input_list)
```

### Let’s take a tuple as input with the input() function. tuple() converts every type of entry (int, float and string) into a tuple of its elements.

``` python
# Taking input from the user as list
input_tuple=tuple(input('Enter a number: '))
print(input_tuple)
```
