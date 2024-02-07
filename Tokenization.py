# -*- coding: utf-8 -*-
"""
Created on Fri May 26 08:21:58 2023

@author: HP
"""
import nltk
nltk.download('punkt')
sentence_data = 'The First sentence is about python. The second sentence is about Django. You can learn python,Django and Data Analysis here'
nltk_tokens = nltk.sent_tokenize(sentence_data)
print(nltk_tokens)

##############################
#Non english Tokenization
import nltk
german_tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
german_tokens = german_tokenizer.tokenize('Wie geht es Ihnen? Gut, danke.')
print(german_tokens)
##################################
#Word Tokenization
import nltk
word_data = "It originated from the idea that there are readers who prefer learning new skills."
nltk_tokens = nltk.word_tokenize(word_data)
print(nltk_tokens)
##################################
import nltk
nltk.download('stopwords')
#IT will download a file with English Stopwords
from nltk.corpus import stopwords
stopwords.words('english')
#The various language other than English which has these stopwords are as the

from nltk.corpus import stopwords
print(stopwords.fileids())

#################################

from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))
all_words = ['There', 'is', 'a', 'tree', 'near', 'the', 'river']
for word in all_words:
    if word not in en_stops:
        print(word)
######################################333333
import nltk
nltk.download('omw-1.4')
from nltk.corpus import wordnet

synonyms = []
for syn in wordnet.synsets("Soil"):
    for lm in syn.lemmas():
        synonyms.append(lm.name())
print(set(synonyms))
#############################################
nltk.download('omw-1.4')
from nltk.corpus import wordnet
antonyms = []
