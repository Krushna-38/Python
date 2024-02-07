# -*- coding: utf-8 -*-
"""
Created on Thu May 25 08:50:05 2023

@author: HP
"""

#cleaning of text
#lets remove all combining charactrs
import unicodedata 
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
b
#Out[16]: 'pýtĥöñ is awesome\n'
b.translate(cmb_chrs)
#Out[17]: 'python is awesome\n'
##################################################

#Yet another technique for cleaning up text involves I/o 
#decoding and encoding functions
a = 'pýtĥöñ is awesome\n'
b = unicodedata.normalize('NFD', a)
b.encode('ascii', 'ignore').decode('ascii')
#Out[19]: 'python is awesome\n'
