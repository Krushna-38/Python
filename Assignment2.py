# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 18:41:03 2023

@author: HP
"""

import pandas as pd
import numpy as np
df = pd.read_csv('Computer_Data.csv')
df
###################################3
#DataFrme Properties
df.shape # (6259, 11)
df.size # 68849
df.dtypes
df.index #RangeIndex(start=0, stop=6259, step=1)
df.columns #Index(['Unnamed: 0', 'price', 'speed', 'hd', 'ram', 'screen', 'cd', 'multi',
       #'premium', 'ads', 'trend'],
      #dtype='object')
df.columns.values
df.describe()
###################################
#Accessing one column content
df['speed']

#Accessing two column content
df[['price','screen']]

######################################
#select certain rows from dataframe and assigned it to another DataFrame
df2=df[6:] #it will select rows from no.6 onwards
df2

df3=df[:2]  #it will print rows of index no.0 and 1
df3

#Accessing certain cell from column
df2 = df['speed'][4]
df2 #It will print row number 4 from DataFrame

#Sutracting specific value from the column
df['speed']=df['speed']-33
df['speed']

#Assign new headers to the columns
df.columns = ['A','B','C','D','F','G','H','J','K','L','M']
df

#Rename Column Names
df.rename(columns={'speed':'Velocity','price':'Value'} ,inplace=True)
df.columns

#Drop rows by index
df2= df.drop(df.index[2])
df2

df2 =df.drop(df.index[[4,6]]) #It will drop multiple rows
df2

#Drop columns by index
print(df.drop(df.columns [2],axis=1))

#Drop columns by using inplace
df.drop(df.columns[[3]], axis=1,inplace=True)
print(df)

#Change the datatypes of multiple columns
df = df.astype({"price":float, "speed":int})
print(df.dtypes)
