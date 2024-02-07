# -*- coding: utf-8 -*-
"""
Created on Tue May 16 08:29:52 2023

@author: HP
"""

##16/05/2023##

#Tokenization#
txt='welcome to the new year 2023'
x=txt.split() #It will split the sentence into the words 
print(x)

#Imports
import re #To remove special characters
def remove_special_characters(text):
    pat= r'[^a-zA-z0-9.,!?/:;\"\'\s]'
    return re.sub(pat, '' , text)

#Call function
remove_special_characters("007 Not sure@ if this% was fun! 223 what do you think# it. is@")

############################################################33
#Remove Numbers#

import re #To remove special characters
def remove_special_characters(text):
    pattern= r'[^a-zA-z.,!?/:;\"\'\s]'
    return re.sub(pattern, '' , text)
#call function
remove_special_characters("007 Not sure@ if this% was fun! 223 what do you think# it. is@")

#####################################
txt ='welcome: to the, new year; 2023'
import re
x=re.split(r'(?:,|;|\s)\s*',txt) 
print(x)
############################

#remove punctuations##
#Imports#
import string
def remove_punctuation(text):
    text=''.join([c for c in text if c not in string.punctuation])
    return text
remove_punctuation('Article :@first sentence of some , {important} article')

###############################################33
#Stemming#
import nltk #Function for stemming
def get_stem(text):
    stemmer = nltk.porter.PorterStemmer()
    text=''.join([stemmer.stem(word) for word in text.split()])
    return text
get_stem("we are dancing and swimming ] ; we have been dancing and swimming ; ")

##########################################
line = 'asdf fjdk; afed, fjek,asdf,foo'
re.split(r'(?:,|;|\s)\s*',line)
##################################
pattern= r'(?:,|;|\s)\s*'
x = re.split(pattern,txt)
print(x)
###############################################
#matching text at the start or end of string
filename='spam.txt'
filename.endswith('.txt')
###########################
area_name='6 th lane west Andheri'
area_name.endswith('west Andheri')
###############################################333
choices= ('http:','ftp:')
url = 'http://www.python.org'
url.startswith(choices)
##########################################
#slicing a string
S = 'ABCDEFGHI' #syntax[start:stop:step]
print(S[2:7])
#slice with negative indices
S= 'ABCDEFGHI'
print(S[-7:-2])
#Slice with positive and negative indices
S = 'ABCDEFGHI'
print(S[2:-5]) 
#Specify the step of the slicing
#Return every 2nd item between position 2 to 7
S = 'ABCDEFGHI'
print(S[2:7:2])
#Returns every 2nd item between position 6 to 1
S = 'ABCDEFGHI'
print(S[6:1:-2])
#Slice first three characters from the string
S = 'ABCDEFGHI'
print(S[:3])
#Slice last three characters from the string
S = 'ABCDEFGHI'
print(S[6:])
#Reverse the String
S = 'ABCDEFGHI'
print(S[::-1])
####################################
#similar operations can be done with slices
filename='spam.txt'
filename[-4:]=='.txt'
###################################3
url = 'http://www.python.org'
url[:5]=='http:'
############################3


#17/05/2023

#########################################
from fnmatch import fnmatch,fnmatchcase
names= ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.csv']
[name for name in names if fnmatch(name, 'Dat*.csv')]
#output:-['Dat1.csv', 'Dat2.csv']
############################################
from fnmatch import fnmatch, fnmatchcase
names =['Andheri East', 'Parle East', 'Dadar West']
[name for name in names if fnmatch(name, '* East')]
#Output:-['Andheri East', 'Parle East']
##########################################
addresses=[
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY']
from fnmatch import fnmatch, fnmatchcase
names =[
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY']
[name for name in names if fnmatch(name, '* ST')]
#Output:-['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
#You could write list comprehensions like this
#################################################
text = 'yeah, but no, but yeah, but no, but yeah'
#Exact match
text == 'yeah'
#False
#match start or end
text.startswith('yeah')
#True
text.endswith('no')
#False
#Search for the location of the first occcurence
text.find('no')
#10
#######################################33
text1 ='11/27/2012'
text2 = 'Nov 27,2012'
 

import re
if re.match('r\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
#yesimport re
if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
#no
#########################################
import re
if re.match('\d{2}-\d{2}-\d{4}', text1):
    print('yes')
else:
    print('no')
    
############################################
import nltk
import re
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
re.sub('python', matchcase('snake'),text, flags=re.IGNORECASE)