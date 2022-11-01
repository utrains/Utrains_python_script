## This code is aimed to define and manipulate strings.

### Create a single line and multiline string, the get its value and type.
``` python
greeeting= "hello everyone!!" # Create an single line string
greetings= '''Hello,
              welcome at Utrains;
            	we are glad to be together during this training''' # Create a multiline string using three single quotes
print(greeeting) # display the value of greeeting
print(greetings) # display the value of greetings
print('The type of the variable greeeting is: ', type(greeeting)) # display the type of variable greeeting
print('The type of the variable greetings is: ', type(greetings)) # display the type of variable greetings
```
### Slice into the string "greeting"
``` python
print('The slicing result of greeting from 2 to 8 index is: ', greeting[2:8]) # normal slicing from index 2 to 8
print('The slicing result of greeting from the start to 10 index is: ', greeting[:10]) # slice from the start
print('The slicing result of greeting from 5 to the end is: ', greeting[5:])  # slice to the end 
print('The slicing result of greeting from -6 to -1 index is: ', greeting[-6:-1]) # Slicing on negatives indexes
```
### Concatenate strings
``` python
firstname="estephe"
surname="Kana"
fullname1= firstname + surname # concatenate firstname and surname without space
print(fullname1)
fullname2= firstname + " " + surname # concatenate firstname and surname with a free space
print(fullname2)
```
### Format strings

### Let's try to concatenate numbers and strings
``` python
number_oranges= 10
bag="The exact number of oranges inside my bag is "+ number_oranges # This will throw an error because we are not concatenate numbers with strigs

### To fix that error, let's use the format() function
bag="The exact number of oranges inside my bag is {}".format(number_oranges) # the format function concatenate integer as a string 
print(bag)
```

