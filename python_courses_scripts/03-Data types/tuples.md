## Just like list, a tuple is also an ordered collection of Python objects.

### The only difference between tuple and list is that tuples are immutable means that  tuples cannot be modified after it is created.

### Let's create some tuples variables and display their content. We'll also see a wrong example of tuple.

``` python
# create a tuple with parentheses
drinks=('water', 'coke', 'beer', 'wine')
mytuple1=(16, 2.5 , "hello", False)

# create a a tuple without parentheses
mytuple2=16, 2.5 , "hello", False

# create a tuple with one item
mytuple3= (6,)

# A tuple with only one item whitout comma is a wrong tuple
mytuple= (6) 

# Display the content of the created variables
print(drinks)
print(mytuple1)
print(mytuple2)
print(mytuple3)
```
### Let's create a tuple contains one item with and without comma; then check the type of each variable

```python
# tuple with comma
course4=("sonarqube",)
print(type(course4)) # python consider it as a tuple: <class 'tuple'>

# tuple without comma
course5=("sonarqube")
print(type(course5)) # python consider it as a string: <class 'str'>

```
### Indexing, slicing, concatenate and multiply tuples

```python
# Let’s create two following tuples as example: 
courseTuple=("linux","kubernetes","docker")
courseMarks= 16, 8, 11

# get the type of courseTuple and courseMarks
print(type(courseTuple))
print(type(courseMarks))

# Indexing (get the first element of courseTuple)
print(courseTuple[0]) # this will display "linux"

# Let's try to change the first element of courseTuple and see the output
courseTuple[0]="sonarqube" # this will throw an error because tuple are immutable

# Slice from the start to index 1 of courseMarks
print(courseMarks[:1])

# Concatenate courseTuple and courseMarks
courseTupleMarks= courseTuple + courseMarks
print(courseTupleMarks)

# multiply the content of courseTuple times 2
courseTupleMultiply= courseTuple * 2
print(courseTupleMultiply)
```
