# -*- coding: utf-8 -*-
"""
Created on Wed May 24 15:05:11 2023

@author: HP
"""

#Normalizing Unicode text to standard representation 
#you're working with unicode strings but need to make sure
#that all of the strings have
#the same underlying representation.
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
s1==s2
#Out[3]: False
#############################################3

#normalisation:- to making your data in uniform pattern
import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
t1==t2
#Out[5]: True
######################################################
#normalisation using NFD
print(ascii(t1))
t3=  unicodedata.normalize('NFD', s1)
t4=  unicodedata.normalize('NFD', s2)
t3==t4
#Out[6]: True
########################################################3

t1 = unicodedata.normalize('NFD', s1)
''.join(c for c in t1 if not unicodedata.combining(c))
#Out[7]: 'Spicy Jalapeno'
###############################
#working with unicode characters in regular Expressions
import re
num = re.compile('\d+')
num.match('123')
pat= re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
pat.match(s)
pat.match(s.upper())
s.upper()
#Out[11]: 'STRASSE'
##########################################
#whitespace stripping
s ='     hello world \n'
s.strip()
#Out[12]: 'hello world' 
###########################################
s ='     hello world      \n'
s.lstrip()
#Out[13]: 'hello world      \n'
##########################3
s ='hello world      \n'
s.rstrip()
#Out[14]:'hello world'
#################################
#character stripping
t = '-----hello===='
t.lstrip('-')
#Out[16]: 'hello===='
t.strip('-=')
#Out[17]: 'hello'

###########################################
