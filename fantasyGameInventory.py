# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:25:53 2022

@author: catal
"""
"""
Fantasy Game Inventory
You are creating a fantasy video game.
The data structure to model the player’s inventory will be a dictionary
where the keys are string values describing the item in the inventory
and the value is an integer value detailing how many of that item the player has.

For example, the dictionary
{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named displayInventory()
that would take any possible “inventory” and display it like the following:


Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
Hint: You can use a for loop to loop through all the keys in a dictionary.


# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
"""


def displayInventory(inventory_dict):
    """assumes inventory_dict is a dictonary with string keys and numeric values
    prints each dictionary as value space key"""
    total_items = 0
    print("Inventory:")
    for key, value in inventory_dict.items():
        print(value, key)
        total_items += value
    print(f"Total number of items: {total_items}")


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)
