# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:12:36 2023

@author: HP
"""

from sklearn.feature_extraction.text import TfidfVectorizer
corpus=["Thor eating pizza, loki is eating pizza, Ironman ate pizza already",
        "Apple is announcing new iphone tommorrow",
        "Tesla is announcing new model-3 tommorrow",
        "Google is announcing new pixel-6 tommorrow",
        "Microsoft is announcing new surface tommorrow",
        "Amazon is announcing new eco-dot tommorrow",
        "I am eating biryani and you are eating grapes"
]
#Let's create the vectorizer and fit the corpus and transform them accordingly
v= TfidfVectorizer()
v.fit(corpus)
transform_output= v.transform(corpus)
#Let's print the vocabulary
print(v.vocabulary_)

#Let's print the idf to each word
all_feature_names = v.get_feature_names_out()

for word in all_feature_names:
    
    #let's get the index in the vocabulary
    indx = v.vocabulary_.get(word)
    #get the score
    