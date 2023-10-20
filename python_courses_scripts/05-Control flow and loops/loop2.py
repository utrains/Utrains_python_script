# Assume you have a list of 5 numbers. Write a script to compute the square of each number using while loop.

index=0
numbers = [1, 3, 5, 8, 12]
while index < len(numbers):
  square = numbers[index] ** 2
  print("Square of:", numbers[index], "is:", square)
  index+=1
  
