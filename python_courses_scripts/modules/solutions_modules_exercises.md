1. If you want to refer to a module by using a different name, you can create an alias. Complete the following code to create an alias for mymodule.

``` python
import mymodule ... mx
```
The correct syntax is:

``` python
import mymodule as mx
```
2. What is the correct syntax of printing all variables and function names of the "mymodule" module?

``` python
import mymodule
print(..........)
```
The correct syntax is:
``` python
import mymodule
print(dir(mymodule))
```
3. What is the correct syntax of importing only the person function of the "mymodule" module?

``` python
.... mymodule ......... person
```
The correct syntax is:

``` python
from mymodule import person
```
4. Write a Python program to generate a random integer between 0 and 6 - excluding 6, random integer between 5 and 10 - excluding 10, random integer between 0 and 10, with a step of 3 and random date between two dates. 
Note: Use random.randrange()

``` python
import random
import datetime
print("Generate a random integer between 0 and 6:")
print(random.randrange(5))
print("Generate random integer between 5 and 10, excluding 10:")
print(random.randrange(start=5, stop=10))
print("Generate random integer between 0 and 10, with a step of 3:")
print(random.randrange(start=0, stop=10, step=3))
print("\nRandom date between two dates:")
start_date = datetime.date(2022, 3, 1)
end_date = datetime.date(2022, 6, 1)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_dt + datetime.timedelta(days=random_number_of_days)
print(random_date)
```
5. Write a Python program to shuffle the elements of a given list. We took two lists (numbers, words) to make an example.
Note: Use random.shuffle()

``` python
import random 
numbers = [1, 2, 3, 4, 5]
print("Original list:")
print(numbers)
random.shuffle(numbers)
print("Shuffle list:")
print(numbers)
words = ['red', 'black', 'green', 'blue']
print("\nOriginal list:")
print(words)
random.shuffle(words)
print("Shuffle list:")
print(words)
```
