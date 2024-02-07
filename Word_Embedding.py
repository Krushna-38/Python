# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:12:54 2023

@author: Krushna Lad
"""

from sklearn.feature_extraction.text import TfidfVectorizer

corpus=['Thor eating pizza, loki is eating pizza, Ironman ate pizza already',
        'Apple is anouncing new iphone tommorow',
        'Tesla is anouncing new model-3 tommorow',
        'Google is anouncing new pixel-6 tommorow',
        'Microsoft is anouncing new surface tommorow',
        'Amazon is anouncing new eco-dot tomorrow',
        'I am eating biryani and you are eating grapes']

#Let's create the vectorizer and fit the corpus and transform them accordingly
v=TfidfVectorizer()
v.fit(corpus)
transform_output=v.transform(corpus)
#let's print the vocabulary

print(v.vocabulary_)
#Lets print the vocabulary

all_feature_names=v.get_feature_names_out()

for word in all_feature_names:
    #let's get the index  in the vocabulary 
    indx=v.vocabulary_.get(word)
    #get the score 
    idf_score=v.idf_[indx]
    print(f"{word} : {idf_score}") 
#################################################3
import pandas as pd

#Read the data into a pandas dataframe
df=pd.read_csv("Ecommerce_data.csv")
print(df.shape)
df.head(5)
#Check the distribution of labels
df['label'].value_counts()
#Add the new column which gives a unique number to each of these lable

df['label_num']=df['label'].map({
    'Household':0,
    'Books':1,
    'Electronics':2,
    'Clothing & Accessoris':3
})

#Checking the results
df.head(5)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    df.Text,
    df.label_num,
    test_size=0.2, #20% samples will go to test dataset
    random_state=2022,
    stratify=df.label_num
)

print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
y_train.value_counts()
y_test.value_counts()
###########################
#Apply to classifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

#1. Create a pipeline object
clf = Pipeline([
    ('vectorizer_tfidf',TfidfVectorizer()),
    ('KNN',KNeighborsClassifier())
])

#2. fit with x_train and y_train
clf.fit(X_train, y_train)

#3. Get the predictions for X_test and store it in y_pred
y_pred = clf.predict(X_test)



