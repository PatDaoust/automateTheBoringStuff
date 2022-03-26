# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 11:57:07 2022

@author: catal
"""
import pyperclip
import re
"""
Get the text off the clipboard.
pyperclip.paste()

Find all phone numbers and email addresses in the text.
regex for phone #s
regex for emails
findall() returns a list of string matches
combine phone #s and emails into string
\n seperated

Paste them onto the clipboard.
pyperclip.copy()\


('Cell: 415-555-9999 Work: 212-555-0000') catalunalilith2680@gmail.com
"""


def extractPhoneEmail():
    """copies string from clipboard
    pastes string to clipboard, only the phone numbers and emails from the copied string
    returns None"""
    text = pyperclip.paste()
    phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
    phone_nums = phone_re.findall(text)
    email_re = re.compile(r"""(
    [a-zA-Z0-9._]+  # username
    @               # @
    [a-zA-Z0-9._]+  # server
    \.              # .
    [a-zA-Z0-9._]+  # domaine
    )""", re.VERBOSE)
    emails = email_re.findall(text)

    # combine phone #s and emails into string
    copy_string = ""
    for match in phone_nums:
        copy_string += match[0] + "\n"
    for match in emails:
        copy_string += match + "\n"
    pyperclip.copy(copy_string)


if __name__ == "__main__":
    extractPhoneEmail()
