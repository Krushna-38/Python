# -*- coding: utf-8 -*-
"""
Created on Thu May 25 08:26:16 2023

@author: HP
"""

#character stripping
t = '------hello====='
t.lstrip('-')  #IT will remove left side elements of the string
#Out[3]: 'hello====='
t = '------hello====='
t.strip('-=') #It will remove both sides elements
#Out[4]: 'hello'
s =' hello world   \n'
s= s.strip()
s.replace(' ', '')
#Out[11]: 'helloworld'
import re
re.sub('\s+', ' ',s)
'hello world'
#############################3
s = 'pýtĥöñ\fis\tawesome\r\n'
s
#Out[12]: 'pýtĥöñ\x0cis\tawesome\r\n'
#The first step isto clean upthe whitespace. Todi this make
# a small translation table
#and use translate():
remap= {
        ord('\t') :' ',
        ord('\f') :' ',
        ord('\r') : None #deleted
        }
a = s.translate(remap)
a
#Out[15]: 'pýtĥöñ is awesome\n'
###########################################333333

