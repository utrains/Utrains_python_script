# This is used to see different ways to import a module functions

#Importing functions module
import functions            
#Calling function add_num defined in functions module.
print(functions.add_num(31,9))

#Importing divide() from functions module
from functions import divide          
#Calling function divide defined in functions module.
print(divide(31,9))

# importing all from functions module
from functions import *
#Calling functions from functions module.
greet()
print(add_num(4, 8))
print(divide(4, 8))
print(add_num(4, 8, 12, 7, 5))   

# rename the functions module as func
import functions as func
#Calling functions from functions module.
func.greet()
print(func.add_num(4, 8))
print(func.divide(4, 8))
print(func.add_num(4, 8, 12, 7, 5))

