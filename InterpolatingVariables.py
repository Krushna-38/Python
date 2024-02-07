# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:15:03 2023

@author: HP
"""

#Interpolating Variables in string
s  = '{name} has {n} messages.'
s.format(name='Guido', n=37)
#Out[26]: 'Guido has 37 messages.'
#####################################3
name = 'Guido'
n = 38
s.format_map(vars())
#Out[29]: 'Guido has 38 messages.'
######################################
