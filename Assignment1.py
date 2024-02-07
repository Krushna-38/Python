# -*- coding: utf-8 -*-
"""
Created on Sat May 27 13:12:37 2023

@author: HP
"""

import pandas as pd
df = pd.read_excel("C:/1-python/Coca.xlsx")
df

#datatypes
df.dtypes
df.astype






###########################################
df.dtypes
cols=["Name","REF","Company_Location","Rating"]
print(cols)
df = df.astype({"Company"==str},errors='ignore')
df
#Properties
df.shape
df.size
df.index
df.dtypes
#Accessing the columns
df[['Company','Name']]


df['Name']

#select certain rows and columns
df2 = df[2:]
df2

#substract from df.rating
df['Rating'] = df['Rating']-10
df['Rating']

#describe
df.describe()
##mean   1035.904735  2012.325348       0.716983    -6.814067
##min       5.000000  2006.000000       0.420000    -9.000000
##max    1952.000000  2017.000000       1.000000    -5.000000

#Rename columns
df.rename(columns={'Company':'Industry','Name':'name'},inplace=True)
df.columns

#Drop rows by index
df1 = df.drop(df.index[1])
df1

#Drop multiple rows
df1 = df.drop(df.index[[1,3]])
df1

#drop columns by name
df2 = df.drop(columns=['Name'], axis=1)
df2

#Drop columns by index
print(df.drop(df.columns[1],axis = 1))

#Using inplace
df.drop(df.columns[[2]],axis=1, inplace=True)
print(df)
#Drop two or more columns
df2 = df.drop(["Industry","name"], axis=1)
print(df2)

#drop two or more columns by index
df = df.drop(df.columns[[0,1]], axis = 1)
print(df2)

#Drop columns from list of columns
lisCol = ["Rating", "Review"]
df2 = df.drop(lisCol, axis= 1)
print(df2)

#Remove columns from DataFrame
df.drop(df.columns[[2]],axis=1, inplace=True)
print(df)

#
df2 = df.iloc[:, 0:2]
df2

################################################
import pandas as pd
import numpy as np 
df = pd.read_excel("C:/1-python/Coca.xlsx")
df
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
print(df)

df2=df.iloc[:,0:2]
df2
#This line uses the slicing  operator to get dataframe
#items by index
df2=df.iloc[0:2,:]
df2
#slicing specific rows and columns using iloc attribute
df3=df.iloc[1:2, 1:3]
df3
##########3
#The second operator [1:3] yields columns 1 and 3only
#select rows by integer index
df2= df.iloc[:,1:3]
df3
#select rows by index
df2=df.iloc[2]
df2
################
df2 = df.iloc[[2,3,6]] #select row by index list
df2 = df.iloc[1:5] #select rows by integer index range
df2 = df.iloc[:1] #select first row
df2 = df.iloc[:3] #select first three row
df2 = df.iloc[:-1] #select last row
df2 = df.iloc[:-3] #select last three row
df2 = df.iloc[::2] #select alternate rows
df2
###select rows by index labels
df2=df.loc['r2'] #select row by index labels
df2
######################3Evening Session
df2 = df.loc[['r2','r3','r6']] #select rows by index label list
df2
df2 = df.loc['r1':'r5'] #select rows by label index range
df2

df2 = df.loc['r1':'r5':2] #select alternate rows with in index
df2
#pandas select columns by name or index
# by using df[] notation
df2 = df['Name']
df2
#select multiple columns
df2 = df[["Name","REF","Rating"]]
df2
#using loc[] to take column slices
#loc[] syntax to slice columns
# select multiple columns
df2 = df.loc[:,["Name","Rating","REF"]]
df2
#select random columns
df2 = df.loc[["Review","Rating","REF"]]
df2
#select columns between two columns
df2 = df.loc[:,'Name':'REF']
df2
##select columns by range
df2 = df.loc[:,'Rating':]
df2
#select columns by range
#All the columns upto 'duration'
df2 = df.loc[:,:'Review']
df2
#select every alternate column
df2 = df.loc[:,::2]
df2

###########################################3
import seaborn as sns
import numpy as np
sns.jointplot(cols)
sns.jointplot()

#Bar Graph
column = list(df['Review'])
print(column)
column.count(0)

column.count(1)

column.count(2)

column.count(3)

column.count(4)

column.count(5)

column.count(7)

import matplotlib.pyplot as plt
fig=plt.figure()
df['Review'].plot(kind='bar')
plt.legend()
