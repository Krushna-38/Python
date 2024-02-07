# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 09:30:41 2023

@author: HP
"""

from fnmatch import fnmatch, fnmatchcase
names = ['Dat1.csv','Dat2.csv', 'config.ini', 'foo.py']
[name for name in names if fnmatch(name, 'Dat*.csv')]
#Out[30]: ['Dat1.csv', 'Dat2.csv']
##############################

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISION ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
    ]
from fnmatch import fnmatchcase
[add for add in addresses if fnmatchcase(add,'* ST')]
#Out[31]: ['5412 N CLARK ST', '1060 W ADDISION ST', '2122 N CLARK ST']
##############################################
text= 'yeah, but no, but yeah, but no, butyeah'
text == 'yeah'
#Out[2]: False
text.startswith('yeah')
#Out[3]: True
text.endswith('no')
#Out[4]: False

#search for the location of the first occurence
text.find('no')
#Out[5]: 10

#######################################
text1= '11/27/2012'
text2='Nov 27, 2012'

import re
#simple matching:\d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
#yes

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
#no

#########################################3

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
if re.match(datepat,text1):
    print('yes')
else:
    print('no')
#yes

if re.match(datepat, text2):
    print('yes')
else:
    
    print('no')
#no
###################################################33
#searching and replacing text
text = 'yeah, but no, but yeah, but no, butyeah'
text.replace('yeah','yep')
#Out[21]: 'yep, but no, but yep, but no, butyep'

#############################################################
#if you have dates in format 11/27/2012 want to convert in 2012-27-11

text= 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re 
re.sub(r'(\d+)/(\d+)/(d+)',r'\3-\1-\2',text)

#Out[24]: 'Today is 11/27/2012. PyCon starts 3/13/2013.'

################################################
#if want to know how many substitutions are made in text then 
#you can use subn() method

newtext, n = datepat.subn(r'\3-\1-2', text)
newtext
#Out[26]: 'Today is 2012-11-2. PyCon starts 2013-3-2.'
##########################################333

text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags=re.IGNORECASE)
#to substitute
re.sub('python','snake', text, flags=re.IGNORECASE)
#Out[27]: 'UPPER snake, lower snake, Mixed snake'

###########################3

#similar as above but using support function
import re
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text.isupper():
            return word.capitalize()
        else:
            return word
    return replace
text3=re.sub('python', matchcase('snake'), text,flags=re.IGNORECASE)
text3
#Out[28]: 'UPPER SNAKE, lower snake, Mixed snake'
####################################

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
str_pat.findall(text1)
#Out[32]: ['no.']

########################################

#However if we have text as below
text2 = 'Computer says "no." phone says "yes."'
str_pat.findall(text2)
#Out[37]: ['no." phone says "yes.']

str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2)

#Out[39]: ['no.', 'yes.']
##################################
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
comment.findall(text1)

#Out[44]: [' this is a comment ']

text2 = '''/* this is a 
           multiline comment */
 '''
comment.findall(text2)
#to fixthe problem you can add support for newlines.
#for example:
comment = re.compile(r'/\*((?:.|\n)*?)\*/')

comment.findall(text2)

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
comment.findall(text2)
###############################################

