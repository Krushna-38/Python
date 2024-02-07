# -*- coding: utf-8 -*-
"""
Created on Tue May 23 08:56:56 2023

@author: HP
"""

import nltk
import re
text= 'UPPER PYTHON, lower python, Mixed Python'
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
####################################################

#Matched the text
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
str_pat.findall(text1)
#['no.']
#However if we have text as below
text2 = 'Computer says "no." phone says "yes."'
str_pat.findall(text2)
#['no." phone says "yes.']
#on finding the longest possible match
str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2)
##############################
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
comment.findall(text1)
#[' this is a comment ']
text2 = '''/* this is a multiline comment */'''
comment.findall(text2)

#To fix the problem, you can add support for newlines.
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)

###################3333
#Remove number from the text
def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result
input_str = "There are 3 balls n this bag"
remove_numbers(input_str)
#######################3
#convert numbers into the word

import inflect
p=inflect.engine()

#convert numbers into word
def convert_number(text):
    #split string into list of words
    temp_str=text.split()
    #initialize empty list
    new_string=[]
    for word in temp_str:
        #if word digit , convert
        if word.isdigit():
            temp=p.number_to_words(word)
            new_string.append(temp)
            
            #append the word as it is
        else:
            new_string.append(word)
    #join the words of new string to form a string
    temp_str=' '.join(new_string)
    return temp_str

input_str='There are 3 balls in this bag and 12 in the'
convert_number(input_str)
    

#######################################################3
#Exercise 1: Reverse each word of a string
str = 'My Name is Jessa'
print(str[::-1])
#################
#iterate ist and reverse each word using ::-1

#Exercise 2:-
a=open('line.txt')
newLine=" "
lines=a.readlines()
for line in lines:
    newLine= newLine +" "+line.rstrip()  

print(newLine)

#############################
#real python.com
#for HW
#



#####################################3

####################################

