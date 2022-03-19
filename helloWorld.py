# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:28:18 2022

@author: catal
"""

# This program says hello and asks for my name.

# name = input("hello, what's your name?\n")
# print(f"hello {name}!")

# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam
# and prints Greetings! if anything else is stored in spam.

spam = "not eggs"

if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")

# Write a short program that prints the numbers 1 to 10 using a for loop.
for num in range(1, 11):
    print(num)

# write an equivalent program that prints the numbers 1 to 10 using a while loop.
num = 1
while num <= 10:
    print(num)
    num += 1

print('Hello', end='')
print('World')
