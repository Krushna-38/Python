# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:21:04 2023

@author: HP
"""

s1= 'Spicy Jalape\u00f1o'
s2= 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
s1==s2
#Out[69]: False

import unicodedata
t1= unicodedata.normalize('NFC',s1)
t2=unicodedata.normalize('NFC',s2)
t1 == t2
#Out[80]: True

##############################################
string1 = "apple"
string2= "jeei125"
string3 = "12345"
string4 = "pre@12"

string1.encode(encoding = 'UTF-8', errors='strict')
string2.encode(encoding = 'UTF-8', errors='strict')
string3.encode(encoding = 'UTF-8', errors='strict')
string4.encode(encoding = 'UTF-8', errors='strict')
##########################################################

text= 'one 🐘 and three 🐋'
print(text)
print(len(text))

e= text.encode('utf8')
print(e)
print(len(e))
#b'one \xf0\x9f\x90\x98 and three \xf0\x9f\x90\x8b'23

e= text.encode('utf16')
print(e)
print(len(e))
#b'\xff\xfeo\x00n\x00e\x00 \x00=\xd8\x18\xdc \x00a\x00n\x00d\x00 \x00t\x00h\x00r\x00e\x00e\x00 \x00=\xd8\x0b\xdc'40

#################################
fname = 'data.txt'
with open(fname, mode='rb') as f:
    contents= f.read()
    print(type(contents))
    print(contents)
    print(contents.decode('utf8'))

#################################
fname = 'data.txt'
with open(fname, mode='rb') as f:
    contents= f.read()
    print(type(contents))
    print(contents)
    print(contents.decode('utf16'))
####################################################


