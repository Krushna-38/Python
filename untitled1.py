# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:50:30 2023

@author: Krushna Lad
"""

import pandas as pd
import numpy as np
#read CSV file
df= pd.read_csv("spam.csv")
#Check first 10 records
df.head()
#TOtal number of  spam and ham
df.category.value_couts()
#Create one more column comprises 0 and 1
#Name of the column is spam
df['spam']=df['category'].apply(lambda x:1 if x=='spam' else 0)
df.shape
#####################################3
#Train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df.Message, df.spam, test_size=0.2)
#let us check the shape of xtrain data and x_text data
x_train.shape
x_test.shape
#let us check the type of x_train and y_train
type(x_train)
type(y_train)
###################################
from sklearn.feature_extraction.text import CountVectorizer
v = CountVectorizer()
x_train_cv= v.fit_transform(x_train.values)
x_train_cv
#After creation of BoW let us check the shape
x_train_cv.shape
###########################################33
#Train the naive_byes model
from sklearn.naive_bayes import MultinomialNB
#Initialize the Model
model = MultinomialNB()
#Train the model
model.fit(x_train_cv, y_train)
##########################################
#Create bag of words representation using CountVectorizer
#of x_test
x_test_cv = v.transform(x_test)
##############################################
#Evaluate Performance
from sklearn.metrics import classification_report
y_pred = model.predict(x_test_cv)
print(classification_report(y_test, y_pred))
