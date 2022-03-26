# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 16:03:06 2022

@author: catal
"""

"""
Strong Password Detection
Write a function that uses regular expressions to make sure the password string
it is passed is strong. A strong password is defined as one that is
at least eight characters long,
contains both uppercase and lowercase characters,
has at least one digit.
test the string against multiple regex patterns to validate its strength.
"""


def validateStrongPassword(password):
    """assumes password is a string
    returns a boolean, True is password is judged to be sufficiently strong,
    else False"""
    pass


if __name__ == "__main__":
    validateStrongPassword("CurryIs#1Cat")
    validateStrongPassword("Curry")
