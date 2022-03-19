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


for num in range(10):
    collatz(num)

"""
Then write a program that lets the user type in an integer
and that keeps calling collatz() on that number until the function returns the value 1. 
(Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)
"""