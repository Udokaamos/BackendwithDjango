# 1.Write a Python program that accepts the radius of a circle from the user and computes the area. 
# 2. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple with those numbers.
# 3. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# 4. Write a Python program to concatenate all elements in a list into a string and return it


#1
import math
r = int(input('Enter radius:\n>'))
print(math.pi * (r**2))

#2
seq = input("Enter numbers seperated by comma:\n>")
to_list = seq.split(',')
to_tuple = tuple(to_list)

#3
name = input("Enter your name:\n>")
print(name[1] + " " + name[0])

#4
elements = ["This", "boy", "is", 2]
elements = list(map(str, elements))
print(" ".join(elements))