# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:21:58 2023

@author: HP
"""

#Text wrapping/Indention
s = 'Look into my eyes, look into my eyes, the eyes, \
    this is india, is this india'
import textwrap
print(textwrap.fill(s, 30))

#################################pr
print(textwrap.fill(s, 40 , initial_indent=' '))
#Look into my eyes, look into my eyes,
#the eyes,     this is india, is this
#india
###########################33
print(textwrap.fill(s, 40, subsequent_indent=' '))
#Output:- Look into my eyes, look into my eyes,
# the eyes,     this is india, is this
# india