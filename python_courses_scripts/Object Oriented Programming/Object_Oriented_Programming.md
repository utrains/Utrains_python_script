## Hands-on of Oriented Object Programming in Python

#### In this document, we are going to show you all the experiments made during the course using OOP Concept 

### Create a class in Python 
A class is a collection of objects. It contains the blueprints or the prototype from which the objects are being created.

#### For example, let's create a class called Circle.

``` python
class Circle:
  pi = 3.14159  # pi is a class attribute
  def __init__(self, radius):
    self.radius = radius # radius is an instance attribute
  # area and circumference are methods 
  def area(self):
    return self.pi * self.radius**2
  def circumference(self):
    return 2 * self.pi * self.radius
```
### Create an Object in Python

#### For example, let's create a new class called Car and three objects from that class.

``` python
# create a class Car with their attributes and methods
class Car:
  def __init__(self, model, price, color, built_year):
    self.model=model
    self.price=price
    self.color=color
    self.built_year=built_year
  def car_details(self):
    print(f'The characteristics of this car are: Model: {self.model}, color: {self.color}, Built year: {self.built_year} and the price is {self.price}')

# create three objects of Car class
car1= Car('AAA', '10K','Orange', 2015)
car2= Car('BBB', '15K','Blue', 2018)
car3= Car('CCC', '45K','Green', 2015)
```
### Access to Object attributes 

#### For example, let's access to car1 attricutes

``` python
# Access to car1 attributes
print(car1.model)
print(car1.price)
print(car1.color)
print(car1.built_year)
```
### Access to Object method 

#### For example, let's access to car1 method

``` python
# Access to car1 method
print(car1.car_details())
```
### Inheritance: create a Parent class and Child Class

**Inheritance** in OOP allows to define a class that inherits all the methods and properties from another class.
**Parent class** is the class being inherited from and **Child class** is the class that inherits from another class.

#### For example, let's Parent and Child class.

``` python
# Create a Parent class "Person"
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
  def isStudent(self):
    return False
# Create a child class "Student" that inherited from "Person"
class Student(Person):
  def isStudent(self):
    return True
```
### Access to Parent and Child Objects

#### For example, let's access to Person and Student Objects

``` python
# create an object "person" from the parent class and access to it
person= Person("John", "Doe")
person.printname()
print(f'Is {person.firstname} a student? {person.isStudent()}')

# create an object "student" from the child class and access to it
student= Student("Estephe","Kana")
student.printname()
print(f'Is {student.firstname} a student? {student.isStudent()}')
```
### Keep a parent class method definition in child class using super()

#### For example, let's use super() to keep the behaviour of the "isStudent" method from sudent class

``` python
class Student(Person):
  def isStudent(self):
    return super().isStudent() # this function super() keep isStudent definition from the parent class
student= Student("Estephe","Kana")
student.printname()
print(f'Is {student.firstname} a student? {student.isStudent()}')
```
### Encapsulation

**The Encapsulation concept** helps to hide and protect attributes and methods which should not be accessed directly.

#### Protected mode: define a variable as protected and try to access to it

``` python
# redefine the class Person with lastname as a protected variable
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self._lastname = lname # set lastname as a protected variable
  def printname(self):
    print(self.firstname, self._lastname)
  def isStudent(self):
    return False

# Let’s try to access to a protected member (lastname) using printname() method
person = Person("John", "Doe")
person.printname()

# Let’s try to access directly to the protected member
person = Person("John", "Doe")
person.lastname
```
#### Private mode: define a variable as private and try to access to it.

``` python
# redefine the parent class with getters and setters
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.__lastname = lname
  def printname(self):
    print(self.firstname, self.__lastname)
  def isStudent(self):
    return False
  def getLastname(self):
    print(f' Person lastname is {self.__lastname}')
  def setLastname(self,lastname_new):
    self.__lastname = lastname_new

# Let’s access to the private member using getLastname() method
person= Person("John", "Doe")
person.getLastname()

# Let’s modify the private member value using setLastname() method
person = Person("John", "Doe")
person.setLastname('Kana')
person.getLastname()
```
### Polymorphism in Inheritance

#### For example, let's change the implementation of child method.

``` python
# let's redefine printname in the parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(f'The firstname of the person is : {self.firstname} and lastname is: {self.lastname}')
    
# change the implementation of printname() in Student class.
class Student(Person):
  def printname(self):
    print(f'The firstname of the student is : {self.firstname} and lastname is: {self.lastname}')
```
### Polymorphism in Inheritance (Accessing to the same method)

#### For example, let's access to the same method with different implementations

``` python
# access to printname() from the parent class
person = Person("Estephe","Kana")
person.printname()

# access to printname() from the child class
student= Student("Estephe","Kana")
student.printname()
```
### Data abstraction in OOP 

#### For example, let's create abstract methods and access to it

create  the Car class that inherited the ABC class and defined an abstract method named mileage() 
and three subclasses(Tesla, Suzuki and Renault) inherited the parent class Car and implemented abstract method differently.

``` python
# Let’s create  the Car class that inherited the ABC class
from abc import ABC  
class Car(ABC):  
  def mileage(self):  #define an abstract method named mileage()
    pass 
    
# define three subclasses(Tesla, Suzuki and Renault) inherited the parent class Car 
# and implemented abstract method differently.
class Tesla(Car):  
  def mileage(self):  
    print("The mileage is 30kmph")  
class Suzuki(Car):  
  def mileage(self):  
    print("The mileage is 25kmph ")  
class Renault(Car):  
  def mileage(self):  
    print("The mileage is 27kmph ")
```
Create three objects to access to abstract methods of subclasses

``` python
# Let’s create three objects to access to abstract methods of subclasses
tesla= Tesla ()  
tesla.mileage()
suziki = Suzuki()  
suziki .mileage()    
renault = Renault()  
renault.mileage()
```
