## A Dictionary is a collection of data which is ordered, changeable and do not allow duplicates.

### Let's create some dictionaries variables and display their type and content

``` python
# create dictionaries variables
student1= {"name":"estephe", "age": 26, "courses":{"linux","git","python"}}
student2= {"name":"john", "age": 19, "courses":{"docker","jenkins","python"}}
student3= {"name":"paul", "age": 30, "courses":{"kubernetes","sonarqube","git"}}

# Display the content and type of the created variables
print(student1)
print(type(student1))
print(student2)
print(type(student2))
print(student3)
print(type(student3))
```
### Access to Dictionaries elements
``` python
# To access to the name of the student1
print(student1["name"])

# We can get the same result by using the method get()
print(student1.get("name"))

# To display a list of all the keys in the student2 dictionary
print(student2.keys())

# # To display a list of all the values in the student3 dictionary
print(student3.values())
```
### Add, update and remove an item of a dictionary

``` python
# Let’s add the item "country" with the value "USA" to student3.
student3["country"]="USA"
print(student3)

# Let’s update the item value of "country" into student3 from "USA" to "Cameroon".
student3["country"]="Cameroon"
print(student3)

# You can also do that by using update() function from "Cameroon" to "France":
student3.update({"country": "France"})
print(student3)

# Let’s remove the item "country" from student3
student3.pop("country")
print(student3)
```
### A Nested Dictionary is a dictionary that contains dictionaries. Let’s create a dictionary "student" that can contains "student1", "student2" and "student3".

``` python
student= {"student1": student1, "student2": student2, "student3": student3}
print(student)
```
