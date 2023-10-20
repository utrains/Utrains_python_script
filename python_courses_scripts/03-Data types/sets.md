## A set  is an unordered collection of data that is iterable, mutable and has no duplicate elements.

### Let's create some lists variables and display their type and content.

``` python
# create a set with same type of data 
myset={'water', 'coke', 'beer', 'wine'}
courseSet1={"linux", "kubernetes", "docker", "jenkins"}
courseSet2={"git", "linux","docker", "sonarqube"}
courseMarks={16, 8, 11, 14, 6, 18,  11, 16}

# create a set with many type of data
myset1={'water', 10, 8.4 , True}

# Display the content of the created variables
print(myset)
print(courseSet1)
print(courseSet2)
print(courseMarks)
print(myset1)

# Display the type of the created variables
print(type(myset))
print(type(courseSet1))
print(type(courseSet2))
print(type(courseMarks))
print(type(myset1))
```
### Accessing sets variables

You can not access set as lists or tuples using index. To access sets, we use for loop as following:

#### Let's show all the elements of the variable myset

``` python
for x in myset:
  print(x)
```

### Add, remove, intersection and union in sets

``` python
# To add an element in the set, we use add() function.
# Let’s add the element "aws" to the set "ourseSet1":
courseSet1.add("aws")
print(courseSet1)

# To remove an element from the set, we use remove() function.
# Let’s remove the element aws from the set courseSet1:
courseSet1.remove("aws")
print(courseSet1)

# To make an intersection between two sets, we use intersection () function. 
# Let’s make an intersection between courseSet1 and courseSet2.
courseIntersect= courseSet1.intersection(courseSet2)
print(courseIntersect)

# To make an union between two sets, we use union() function.
# Let’s make an union between courseSet1 and courseSet2.
# Duplicates are excluded.
courseUnion= courseSet1.union(courseSet2)
print(courseUnion)
```
