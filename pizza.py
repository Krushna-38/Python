# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 09:28:16 2023

@author: HP
"""

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{toppings}")