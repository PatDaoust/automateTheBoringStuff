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
# displayInventory(stuff)


"""
Imagine that a vanquished dragon’s loot is represented as a list of strings like this:


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems),
where the inventory parameter is a dictionary representing the player’s inventory
(like in the previous project) and the addedItems parameter is a list like dragonLoot.
The addToInventory() function returns a dictionary that represents the updated inventory.
Note that the addedItems list can contain multiples of the same item.
Your code could look something like this:


def addToInventory(inventory, addedItems):
    # your code goes here

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
The previous program (displayInventory()) would output the following:


Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48
"""


def addToInventory(inventory_dict, loot_list):
    """assumes inventory_dict s a dictonary with string keys and numeric values
    assumes loot_list is a list of strings
    returns a dict, an updated inventory including the loot
    does not mutate the original inventory_dict
    warning: strings from loot_list and inventory_dict must match exactly"""
    new_inventory = dict(inventory_dict)
    for item in loot_list:
        new_inventory.setdefault(item, 0)
        new_inventory[item] += 1
    return new_inventory


dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
updated_inventory = addToInventory(stuff, dragon_loot)
displayInventory(updated_inventory)
