# Data types: solutions of exercises

1. Give the type of each of the following data:

``` python 
data1=[1, 6, "number", 10.6, True]
data2=-21
data3={"lesson": "Python", "Course": "variables and data types", "section": "data types"}
data4= False
data5=("dog", "cat", "eagle","lion")
data6=100.87
data7="Good morning"
data8={"linux", "windows","Mac OS"}
```
* **data1** is a list
* **data2** is an integer
* **data3** is a dictionary
* **data4** is a boolean
* **data5** is a tuple
* **data6** is a float
* **data7** is a string
* **data8** is a set

2. Convert data6 into integer then summarize it with data2.

``` python 
# Convert data6 into integer
data6_int= int(data6)
print(data6_int)

# summarize data6_int with data2 
data_sum= data6_int + data2
print(data_sum)
```
3. Give the command to show the last three elements of data1.

``` python 
print(data1[2:])
```
4. Add data2, data4, data6 and data7 into data1.
``` python 
data1.append(data2)
data1.append(data4)
data1.append(data6)
data1.append(data7)
print(data1)
```
5. Convert data8 to a tuple and combine it with data5.

``` python 
# convert data8 to tuple
data8_tuple= tuple(data8)
print(data8_tuple)

# combine data8_tuple and data5
data_comb= data8_tuple + data5
print(data_comb)
```
6. Slice into data7 and get the word "morning".

``` python 
print(data7[5:])
```
7. Convert data7 in uppercase and lowercase using its methods.

``` python 
# convert data7 in uppercase
data7_upper= data7.upper()
print(data7_upper)

# convert data7 in lowercase
data7_lower= data7.lower()
print(data7_lower)
```
8. Remove the first two items of data1.

``` python 
data1.pop(0) # to remove the first element
data1.pop(0) # we still use 0 because the second element becomes the first
print(data1)
```
9. Use negative indexing to print the last third element of data5

``` python 
print(data5[-3:])
```
10. Remove the item “Mac OS” from data8

``` python 
data8.remove('Mac OS')
print(data8)
```
11. Change "course" value from "variables and data types" to "Python data types" in data3.

``` python 
data3.update({'Course': 'Python data types'})
print(data3)
```
12. Use the pop method to remove "section" from data3

``` python 
data3.pop("section")
print(data3)
```
