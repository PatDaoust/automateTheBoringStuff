# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 19:18:44 2022

@author: catal
"""

# pw.py - An insecure password locker program

import pyperclip

password_dict = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
                 'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
                 'luggage': '12345'}


def main(account_name):
    """assumes account_name is a string, representing an account name
    returns None
    outputs a string to the clipboard"""
    if not account_name:
        print("Your input must consist of at least one character. Please try again.")
        return
    if account_name not in password_dict:
        print("I don't have an account by that name")
        return
    password = password_dict[account_name]
    # copy password to clipboard
    pyperclip.copy(password)


if __name__ == "__main__":
    message = "Please input the name of the account whose password you wish to retrieve\n"
    main(input(message))
