# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 19:17:03 2022

@author: catal
"""


def collatz(number):
    """assumes number is an int
    If number is even, prints and returns number // 2
    If number is odd, prints and returns 3 * number + 1
    """
    if number % 2 == 0:
        collatz = number // 2
    else:
        collatz = (3 * number) + 1
    print(collatz)
    return collatz


# for num in range(10):
#     collatz(num)

"""
Then write a program that lets the user type in an integer
and that keeps calling collatz() on that number until the function returns the value 1
"""


def collatzSequenceFinder():
    """asks for user input
    stops when a collatz value of 1 is found"""
    start = (input("please type the seed number to start your collatz search\n"))
    try:
        start = int(start)
    except ValueError:
        print("I'm sorry, that doesn't seem to be a valid number")
    result = start
    while result != 1:
        result = collatz(result)


# collatzSequenceFinder()
