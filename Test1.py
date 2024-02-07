# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:04:04 2023

@author: HP
"""
#Write a python function that takes two lists and returns True if they 
#atleast one common member.

def lst(a,b):
    for i in a:
        for j in b:
            if i==j:
                return True
lst([1,2,3,4,5],[9,6,78,8,1])

#Use list comperhension to construct a new list but add 6 to each item

list1=[1,2,3,4,5,6]
list2=[i+6 for i in list1]
print(list2)

#write a python program to reverse a string
string="Krushna"
print(string[::-1])

#write a python program to iterate over dictionaries using for loop
capitals={"Maharashtra":"Mumbai",
          "UP":"Luknow",
          "Gujrat":"Gandhinagar"}
print(capitals)

for i in capitals.keys():
    print(i)
for i in capitals.values():
    print(i)
    
#using ictionary comperhension and conditional argument createa dictionary 
#from the current dictionary where only the keyvalue pairs with above 2000 are 
#taken to the new dictionary
dict1={
       'A': 1,
       'B': 2,
       'C': 3999,
       'D': 4888
       }
print(dict1)
dict2={
       i:j
       for i in dict1.keys()
       for j in dict1.values()
       if j > 2000
       }
print(dict2)

#############################
with open('C:/1-python/Decorators.txt') as f:
    a=f.readlines()
print(a)

#
list1=[1,2,3,4,5,6,7,8,9]
list2=[i for i in list1 if i%2==0]
print(list2)

list3=[i for i in list1 if i%2==1]
print(list3)

#Q.9
import pandas as pd 
dictionary={'name':['Anna','Dinu','Ramu','Ganu','Sonu','Monu'],
            'attempts':[1,2,3,3,4,5,]}
df=pd.DataFrame(dictionary)
df

#Q.10
