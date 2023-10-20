## Lists are just like the arrays, declared in other languages which is a ordered collection of data.

### Let's create some lists and display their content

``` python
# create a list with same type of data 
drinks=['water', 'coke', 'beer', 'wine']

# create a list with many type of data
mylist=["orange",14, 25.4, True, 'hello']

# Display the content of the created variables
print(drinks)
print(mylist)
```
### Check type and length of some lists take as example and accessing elements of those lists by index


``` python
# let's take the following lists as example:
courseList=["linux", "kubernetes", "docker"]
courseMarks=[16, 8, 11]

# check type of courseList and courseMarks
type(courseList)
type(courseMarks)

# check length of courseList and courseMarks
print(len(courseList))
print(len(courseMarks))

# Access to the second element of courseList, and the first and second element of courseMarks

print(courseList[1]) # the index 1 represtents the second element of courseList 
print(courseMarks[0]) # the index 0 represtents the first element of courseMarks 
print(courseMarks[1]) # the index 1 represtents the second element of courseMarks 
```
### Append and pop element in a list

``` python
# Take courslist, we previously created as example.

# Let’s add a course jenkins into the list courseList:
courseList.append("jenkins")

# Let’s remove the second element of the list courseList:
courseList.pop(1)
```
### Slicing lists
``` python
# Take courslist and courseMarks, we previously created as example.

# Grab between index 0 and index 2 for courseList:
print(courseList[0:2])

# Grab index 1 and everything past it for courseMarks:
print(courseMarks[1:])

# Grab everything up to index 2 for courseList:
print(courseList[:2])
```
### Concatenate lists in Python

``` python
# Take courslist and courseMarks as examples

# Let’s concatenate courseList and courseMarks, to obtain a list named courseListMarks.

courseListMarks= courseList + courseMarks
print(courseListMarks)
```
