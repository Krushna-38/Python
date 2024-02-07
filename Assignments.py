# -*- coding: utf-8 -*-
"""
Created on Wed May  3 19:29:21 2023

@author: HP
"""
##03/05/23
import pandas as pd
df = pd.read_csv('AutoInsurance.csv')
df.shape
df.size
df['State']
df[['State','Gender']]
df.describe()
#select certain rows and assign it to another dataframe
df2=df[5:]
df2
#accessing certain cell from dataframe
df['Coverage'][15]
#rename pandas dataframe columns using rename()
df = df.rename({'State':'A','Coverage':'K'})
df = pd.read_csv("AutoInsurance.csv")
#drop rows by index position
df2 = df.drop(df.index[1:])
df2

##Drop column by column name
df2 = df.drop(['Customer'],axis=1)
df2

##Ignoring Error
df = df.astype({'Gender':int},errors='ignore')
df.dtypes
#####
#generate Error
df= df.astype({'Gender':int},errors='raise')
df.dtypes

#########3
#change type for4 one or multiple columns
df = df.astype({'Income':int,'Customer Lifetime Value':float})
print(df.dtypes)

###########################
#########################
#ASSIGNMENT 04/05/2023#
import pandas as pd
df = pd.read_csv('boston_data.csv')
df
df.shape #To get the shape of DataFrame(404, 14)
df.size   # To get the size of the DataFrame(5656)
df['crim'] # Access single column from DataFrame
df[['crim','zn']] #Access multiple columns
df.describe() #FOr describe DataFrame
#rename pandas dataframe columns using rename()
df = df.rename({'crim':'A','zn':'K'})
df = pd.read_csv("boston_data.csv")
df
#drop rows by index position
df2 = df.drop(df.index[1:])
df2
##Drop column by column name
df2 = df.drop(['zn'],axis=1)
df2
##Ignoring Error
df = df.astype({'crim':int},errors='ignore')
df.dtypes
#generate Error
df= df.astype({'indus':int},errors='raise')
df.dtypes
#change type for4 one or multiple columns
df = df.astype({'rm':int,'rad':float})
print(df.dtypes)

#Drop two or more columns by label name
df2 = df.drop(["zn","rad"], axis=1)
df2
#drop column by index
print(df.drop(df.columns[[1]], axis=1))

#iloc
df = pd.DataFrame(boston_data, index=row_labels)
df
