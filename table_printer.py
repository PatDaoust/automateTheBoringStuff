# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:12:32 2022

@author: catal
"""
"""
Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
"""

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def tablePrinter(list_list):
    """assumes list_list is a list of lists of strings,
    where the inner lists are all of the same lenght
    prints list_list in table for
    returns None"""
    # find max lenght items and add padding
    for i in range(len(list_list)):
        max_len = 0
        for outer_list in list_list:
            if len(outer_list[i]) > max_len:
                max_len = len(outer_list[0])
        for outer_list in list_list:
            len_dif = max_len - len(outer_list[i])
            if len_dif > 0:
                outer_list[i] = (" " * len_dif) + outer_list[i]
    # print table
    for row in list_list:
        print(row)


if __name__ == "__main__":
    tablePrinter(table_data)
