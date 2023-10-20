## Boolean variables in python has just two values assigned to it, "True" or "False".

### Let's define some boolean variables and display their content
```python
boolean1= 7 > 7.5
boolean2= 7 == 7.5
boolean3= 7 < 7.5

# display the content of each of those variables.

print(boolean1) # False
print(boolean2) # False
print(boolean3) # True
```
### Non-Boolean objects can be evaluated in Boolean context as well and determined to be True or False. The built-in function bool() is used to evaluate them. It returns True for most of values except empty ones.

```python
print(bool("Hello")) # True
print(bool(15)) # True
print(bool("")) # False
```
### Note: True and False with capital ‘T’ and ‘F’ are valid booleans otherwise python will throw an error.
```python
print(type(True)) # <class 'bool'>
print(type(False)) # <class 'bool'>
print(type(true)) # This will throw an error
```
