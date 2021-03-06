# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 14:55:43 2022

@author: catal
"""

"""Say you have a list value like this:


spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and
returns a string with all the items separated by a comma and a space,
with and inserted before the last item.
For example, passing the previous spam list to the function would return
'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.
"""


def commaCode(a_list):
    """assumes a_list is a list of strings
    returns a string, the contents of a_list with ", " between items"""
    result_str = ""
    for i in range(len(a_list)-1):
        result_str += a_list[i] + ", "
    result_str += "and " + a_list[-1]
    return result_str


spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaCode(spam))
