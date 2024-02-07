# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:44:43 2023

@author: HP
"""

#Pip install ensim
#Pip install python-Levenshtein
import gensim
import pandas as pd
df = pd.read_json(r"C:/Dataset/Cell_Phones_and_Accessories_5.json",lines=True)
df
df.shape
#Simple Preprocessing And Tokenization
review_text= df.reviewText.apply(gensim.utils.simple_preprocess)
review_text
#Let us check first word of each review
review_text.loc[0]
#LEt us check first row of dataframe
df.reviewText.loc[0]
#Training the word2vec model
model = gensim.models.Word2Vec(
    window=10,
    min_count=2,
    workers=4,
)
"""
where window is how many words you are going to 
consider as sliding window you can choose any count
min_count-there must min 2 words in eacch sentence 
workers:no.of threads
"""

#Build Vocabulary
model.build_vocab(review_text,progress_per=1000)
#Progress_per:after 1000 words it shows progress
#Train the Word2Vec model
#It will take time,have patience
model.train(review_text,total_examples=model.corpus_count,epochs=model.epochs)
#Save the model
model.save("C/Dataset/20-text_mining./word3vec-amazon-cell-accessories-reviews-short.model")
#Finding similar words and similarity between words
model.wv.most_similar("bad")
model.wv.similarity(w1="cheap", w2="inexpensive")
model.wv.similarity(w1="great",w2="good")
