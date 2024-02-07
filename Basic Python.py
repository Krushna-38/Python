# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:57:55 2023

@author: HP
"""

"""
Basic of Python 

@author : Sachin Borade
"""
print("HELLO")
x = 1; 
print(x)
print(type(x))

age1 = input("Enter the age")
print(type(age1))

age2 = input("Enter the age")
print(type(age2))

print(age1 + age2)

age1 = int(input("Enter the age"))
print(type(age1))

age2 = int(input("Enter the age"))
print(type(age2))

print(age1 + age2)

int_value = 100
print(type(int_value))

float_value=float(int_value)
print(float_value)


#complex number

c1 = 1
c2 = 2j
print(c1.real)
print(type(c1))
print(c2.imag)
print(type(c2))

#Boolean Data type

its_ok = True
print(its_ok)

#type casting
status = bool(input("Enter the status:-"))
status = False
print(status)
print(type(status))

home = 10
away = 15

print(home + away)
print(type(home + away))
print(10 * 15)
print(type(10 * 15))
#the division of interger is always a float 
print(100/20)
print(type(100/20))

#to convert division into interger use " // "
print(100//20)
print(type(100//20))


#If we want remainder then there is modulus operator 
print(4 % 2)

a = 2
b = 5
print(a ** b)

# How to Declare the None
winner = None
print(winner is None)
print(winner is not None)

#Identation 
#If else statement
a = int(input("Enter the number:-"))
if a > 0:
    print("It is positive number")
else:
    print("It is 0 or negative number")
    
# If elif else statement execution
b = int(input("Enter the number"))
if b > 0:
    print("Positive")
elif b == 0:
    print("It is zero")
else:
    print("It is negative")
    
#looping statements
#while loop
c = 0
while(c < 10):
    print(c)
    c+=1
#for loop 
for i in range(0,10):
    print(i)
#for loop 
for i in range(10,0,-1):
    print(i)
#breaking statement
#break 
for i in range(1,11):
    if i == 5:
        break
    else:
        print(i)
        
#continue 
for i in range(1,11):
    if i == 5:
        continue
    else:
        print(i)
        
#anonymous loop variable
for _ in range(1,5):
    print(".",end=" ")


height = float(input("Enter you height in metere: "))
weight = float(input("Enter you weight in kg: "))
BMI = round((weight/ (height * height)),2)
if BMI < 18.5:
    print(f"You are under weight and your BMI is: {BMI}")
elif BMI > 18.5 and BMI < 25:
    print(f"You are normal weight and your BMI is: {BMI}")    
elif BMI > 25 and BMI < 30:
    print(f"You are over weight and your BMI is: {BMI}")
elif BMI > 30 and BMI <35:
    print(f"You are obese and your BMI is: {BMI}")
else:
    print(f"You are clinically obese and you BMI is: {BMI}")

    
#checking the you are ellible for roller coaster or not

#height = int(input("Enter your height"))
#if height >= 120:
#    print("You are elligible for rollar coaster")
#    age = int(input("Enter your age:-"))
    
#    if age >= 12 and age <= 18:
#        print("You are elligible and ticket price is: {")
#    elif age >= 18 and age <=45:
    
#    elif age >=45  and age <=55:
    
#    elif
    
    
#break statement 

num = int(input("Enter the Number:-"))
for i in range(0,6):
    if num == i:
        break
    print(i,end=" ")

#creating the tuple 
tup = (1,3,4,5,6)
print(tup[0])

#to iterate over tuple using tup
for i in tup:
    print(i,end=" ")
    
# to iterate over tuple using range function
for i in range(0,5):
    print(i,end=" ")
    
tup2=(1,1,2,3,4,5,6)
#len function gives the legth of tuple
len(tup2)

#to find the index specific number
tup2.index(3)

#to count which specific element is repeated
tup2.count(1)


#We can have tuple in tuple (Nested Tuple) 
tup3 = ('apple','orange','banana','papaya',(3,2))
print(tup3)

if 'apple' in tup3:
    print("apple is present ")
else:
    print("apple is not present")


#List have positive as well as negative indexing 
lst = [1,2,4,5,5,6]    
#positive indexing
for i in range(0,len(lst)):
    print(lst[i],end=" ")
    
#negative indexing
lst = [1,2,4,5,5,6]
for i in range(5,-1,-1):
    print(lst[i],end=" ")

#inserting the element at the last in the list
lst.append(7)
print(lst)     

lst1 = [7,8,9,10,11]
 
#list in to list (Nested List) we can make
lst.extend([lst1])
print(lst) 
#We can also extend the list using extend keyword
lst.extend(lst1)
print(lst)   

#we can also add at specific index
lst.insert(1,0)
print(lst)


#Find the duplicate in the list
lst2 = [1,2,3,1,5,1]
for i in range(len(lst2)-1):
    for j in range(len(lst2)-1):
        if i  != j:
            if(lst2[i]  == lst2[j]):
                print("THe duplicate is:-",lst2[i])
    
#Prining the Mario Pyramid reverse
n = int(input("Enter the number:-"))
for i in range(n,0,-1):
    for j in range(0,i):
        print('#',end=" ")
    print("\n")  
#Printing the Mario Pyramid forward order
for i in range(1,n+1):
    for j in range(0,i):
        print("#",end=" ")
    print("\n")

#printing the star pattern 
a = int(input("Enter the number:-"))
m = (a * 2) - 1
for i in range(0,m):
#Paliandrome
# palimdrome python progrom
a=input("Enter the data : ")
def palimdrome(a):
    if a == a[::-1]:
        print("It is palimdrome string ")
    else:
        print("It is not palimdrome string ")
palimdrome(a)
#minimum maxium
def minimum(lst0):
    g = lst0[0]
    for i in range(len(lst0)):
        if lst0[i] < g:
            g = lst0[i]
    return g

def maximum(lst0):
    g = lst0[0]
    for i in range(len(lst0)):
        if lst0[i] > g:
            g = lst0[i]
    return g

lst7 = [6,8,24,3,83]
print(minimum(lst7))
print(maximum(lst7))

#list
lst = ['sachin','gaurav','gavrav','prathamesh','vaibhav']
#remove method
lst.remove('gavrav')
#pop method
lst.pop()
#insert method
lst.insert(4,'Vaibhav')
print(lst)
#concatenation of the list
lst5 = [6,8,24,3,83]
lst6 = [1,2,3,1,5,1]
lst8 = lst5 + lst6
print(lst8)

#set
lst3 = {1,2,3,1,5,1}
print(lst3)
print("Maximum")
print(max(lst3))
print("Minimum")
print(min(lst3))
#interative over the set using for loop
for _ in lst3:
    print(_,end=" ")
#Adding item to the set
lst3.add(4)
print(lst3)
ser0 = {'sachin','gavrav'}
#update item to the set
ser0.update({'ram','tushar','vaibhav'})
print(ser0)
  
#set operation
s1 = {1,2,3,1,5,1}  
s2 = {6,8,24,3,83}

print("Union",s1 | s2)
print("Intersection",s1 & s2)
print("Difference",s1 - s2)
#Dictonary

capitals = {
    'Maharashtra':'Mumbai',
    'Gujrat':'Gandhinagar',
    'Punjab':'Chandigad',
    'Hariyana':'Chandigad'
    }
print(capitals)

#Accessing the Value using key
print(capitals['Maharashtra'])

#Addding the new Entry
capitals['West_Bengal'] = 'Kolkata'
print(capitals)

#Deleting the entry from dictonary
capitals.pop('Maharashtra')
print(capitals)
print(capitals.values())

# "in" and "not in" operator
#Its gives the output is in boolean form
print('Maharashtra' in capitals)


#Dictonary can have values like Tuple and List
season = {'summer':('feb','mar','apr','may'),
          'rainy':('june','july','aug','sept',),
          'winter':('oct','nov','dec','jan')}
print(season['summer'])
print(season['rainy'][1])
print(season['winter'])

#Dictonary dont allow the dupicate in it
dict2 ={
        'brand':'maruti',
        'model':'Brezza',
        'year':2020,
        'year':2022
        }
print(dict2)

#Iterate using loop
for _ in dict2.values():
    print(_)
for _ in dict2.keys():
    print(_)

def add(a,b=2,c=0):
    print(a,b,c)
add(5,c=8)