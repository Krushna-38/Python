# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 08:14:10 2023

@author: HP
"""

#Q.1
def empty(list):
    if(len(list)==0):
      print("list is empty")
    else:
        print("list having elements")
        
empty([22,334])
empty([])

#Q.2
a=[4,5,6]
b=[i*i for i in a]
print(b)

#Q.3
dict={'a':'Ramu','b':'Ganu','c':'Sham'}
f=dict.keys()
g=list(f)
for i in range(len(g)):
    if dict[i]==key:
        print("key is present")
        break
    else:
        print("key is not present")
        
#Q.4
r=range(100,160,10)
b={i:r[i] for i in range(len(r))}
print(b)

#Q.5

import pandas as pd
k= {
     'course':['Python','Java'],
     'fees':[1112,3344],
     'duration':[3232,3232]}
df=pd.DataFrame(k)
df
df['tutor']=[2,3,]
df
##Q.6
df.to_csv('krish.csv')


#Q.7
def function(*a):
   return f'the value is{a}'
function(2,3,'abc',5,[2,3])
    
#Q.8
d=lambda a,b:a*b
d(5,5)

#Q.9
import numpy as np

k=np.array([0])
k.any()
j=np.array([2,3])
j.any()

#Q10
import matplotlib.pyplot as plt
xlabel=[1,2,3,4]
ylabel=[25,2,31,4]
plt.plot(xlabel,ylabel)
plt.plot(marker_style='Dot',marker_line='Dashed')


#Q.11
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
k={"Languages":['Java','Python','PHP','JavaScript','C#','C++'],
"Popularity":[22.2,23.7,8.8,8,7.7,6.7]}
df=pd.DataFrame(k)

df
plt.bar(df['Languages'],df['Popularity'])