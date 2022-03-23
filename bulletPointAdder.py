# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 12:09:27 2022

@author: catal
"""
import pyperclip


def bulletPointAdder():
    """gets the text from the clipboard
    adds a star and space to the beginning of each line
    pastes this new text to the clipboard
    returns None
    """
    text = pyperclip.paste()
    text_list = text.split("\n")
    mod_list = []
    for sub_text in text_list:
        sub_text = "* " + sub_text
        mod_list.append(sub_text)
    mod_text = "".join(mod_list)
    pyperclip.copy(mod_text)


if __name__ == "__main__":
    bulletPointAdder()
