# -*- coding: utf-8 -*-
"""
Created on Fri May 26 14:49:05 2023

@author: HP
"""
#Name:- Krushna Lad
#Dept:- Electrical


import pandas as pd
df=pd.read_csv("C:/1-python/DataAttendance.csv")
df2 = df.rename(columns = {'Krushna Lad':'Krushna_Lad'})
print(df2)


# 1.Rename the column name 
df.rename(columns={'Krushna lad':'lad_Krushna'},inplace=True)
df.columns
print(df)
df = df.rename({'Krushna Lad':'Krushna_Lad'})
df
df.columns
df.rename({'Krushna lad':'lad_Krushna'},axis=1)
df.columns
#Remove columns from dataFrame
df.drop(df.columns[1:61], axis=1,inplace=True)
df
# 2.Convert column into list
column= list(df['Krushna Lad'])
print(column)

# 3. for 0,1,2,3,4,5,7

column.count(0)

column.count(1)

column.count(2)

column.count(3)

column.count(4)

column.count(5)

column.count(7)

# 4. Bar Graph for attendance
import matplotlib.pyplot as plt
fig=plt.figure()
df['Krushna Lad'].plot(kind='bar')
plt.legend()


# 5.describe()
df['Krushna Lad'].describe()

# 6.Generate box plot using seaborn for your column and write the inference
import seaborn as sns
sns.boxplot(df['Krushna Lad'])


# Q.7 Generate joint plot using seaborn for your column and write the inference
import seaborn as sns
sns.jointplot(column)
sns.jointplot()
  
# Q. 8 From complete dataframe, find out how many are regular students, how many are moderate and
#how many are poor in attendance.
df=df.iloc[27]
df
print(df.max())


"""
MArksheet.csv
"""

import pandas as pd
df=pd.read_csv("C:/1-python/Marksheet.csv")
df
df.columns

# 9. Out of functions, list and dictionary ,in which area you are strong and weak?
df2=df.iloc[45]
df2.max
df2
df2.column

print(df.max())
df2.max

#Q.10 How many students have shown very good performance and how many have shown poor performance
# Assuming you have a list or array of performance scores
column= list(df['Total'])
print(column)
performance_scores = [0, 0, 2, 4, 4, 6, 2, 4, 2, 6, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 0, 6, 2, 2, 2, 6, 6, 4, 6, 6, 6, 4, 6, 4, 6, 10, 6, 8, 8, 8, 8, 8, 8, 6, 6, 8]

# Define the threshold values for very good and poor performance
very_good = 5
poor = 5

# Count the number of students with very good and poor performance
very_good_count = len([score for score in performance_scores if score >= very_good])
poor_count = len([score for score in performance_scores if score < poor])

# Print the results
print("Number of students with very good performance:", very_good_count)
print("Number of students with poor performance:", poor_count)

#Open the given file in read mode
file_path = "C:/1-python/AI.txt"  
with open(file_path, "r") as file:
    file_contents = file.read()
file_contents

#Remove numbers from text
import re

def remove_numbers(text):
    pattern=r'[^a-zA-z.,!?/:;\"\s]'
    return re.sub(pattern, '',text)

remove_numbers(file_contents)

# How many companies were surveyed ,extract using text processing

with open(file_path) as file_object:
    data = file_object.read()
    num=re.findall(r'\d+(?:\.\d+)?',data)
    print(num)
    num[0]

# Q.14 How many companies are willing to shift in AI domain,extract using text processing.
with open(file_path) as file_object:
    data = file_object.read()
    num=re.findall(r'\d+(?:\.\d+)?',data)
    print(num)  
    print("Percentage of companies:",num[-8])

# Q.15 How many millions jobs are expected to create in 2024 in field of AI
with open(file_path) as file_object:
    data = file_object.read()
    num=re.findall(r'\d+(?:\.\d+)?',data)
    print(num)
    num[-1]

# .16 Convert numbers into words
import inflect
p=inflect.engine()
def convert_number(text):
    temp_str=text.split()
    new_string=[]
    for word in temp_str:
        if word.isdigit():
            temp=p.number_to_words(word)
            new_string.append(temp)
        else:
            new_string.append(word)
    temp_str=' '.join(new_string)
    return temp_str


convert_number(file_contents)

###############################################################33

