# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 16:03:06 2022

@author: catal
"""
import re
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
    # is 8+ chars
    re_8chars = re.compile("(.){8,}")
    if not re.search(re_8chars, password):
        return False
    # uppercase and lowercase
    re_upper = re.compile("[A-Z]")
    if not re.search(re_upper, password):
        return False
    re_lower = re.compile("[a-z]")
    if not re.search(re_lower, password):
        return False
    # digit
    re_digit = re.compile("\d")
    if not re.search(re_digit, password):
        return False
    return True


if __name__ == "__main__":
    pass
    # print(validateStrongPassword("CurryIs#1Cat"))
    # print(validateStrongPassword("Cu1"))
    # print(validateStrongPassword("curryis#1cat"))
    # print(validateStrongPassword("CURRYIS#1CAR"))
    # print(validateStrongPassword("CurryIsCat"))
