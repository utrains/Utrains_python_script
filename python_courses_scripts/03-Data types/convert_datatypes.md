## We can convert different data types by using different types of conversion functions like int(), float(), str(), etc.

### To convert an integer to float, we use float() function:
``` python
my_int1=9
print(type(my_int1))
my_float1=float(my_int1) # convert the integer 9 to float 9.0
print(my_float1)
print(type(my_float1))
```
### To convert a float to int , we will truncate the value (make it closer to zero). To do that, we use int() function:
``` python
my_float2= 67.6
print(type(my_float2))
my_float3= -67.6
print(type(my_float3))
my_int2=int(my_float2) # convert the float 67.6 to integer 67
print(my_int2)
print(type(my_int2))
my_int3=int(my_float3) # convert the float -67.6 to integer -67
print(my_int3)
print(type(my_int3))

```
### Conversion between float and string

``` python
# from string to float
my_string1= '67.6'
print(type(my_string1))
my_float2=float(my_string1) 
print(my_float2)
print(type(my_float2))

# from float to string
my_float2= 67.6
print(type(my_float2))
my_string1= str(my_float2)
print(my_string1)
print(type(my_string1))
```
### Conversion of one sequence (tuple, set, list) to another.

``` python
# convert a list to a set
my_list1= [1,2,3]
print(type(my_list1))
my_set1=set(my_list1)
print(my_set1)
print(type(my_set1))

# convert a set to tuple
my_set1={4,5,6}
print(type(my_set1))
my_tuple1= tuple(my_set1)
print(my_tuple1)
print(type(my_tuple1))

# convert a string to list
my_string2= 'Morning'
print(type(my_string2))
my_list2 = list(my_string2)
print(my_list2)
print(type(my_list2))
```
### To convert to dictionary, each element must be a pair. Let's convert some lists to dictionaries

``` python
# convert a nested list to a dictionary
my_list3= [[7,8],[9,10]]
print(type(my_list3))
my_dict1= dict(my_list3)
print(my_dict1)
print(type(my_dict1))

# convert a list of tuples to dictionaary
my_tuple_2= [(2,21),(4,47)]
print(type(my_tuple_2))
my_dict2= dict(my_tuple_2)
print(my_dict2)
print(type(my_dict2))

```

