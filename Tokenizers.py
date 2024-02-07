# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:03:06 2023

@author: Krushna Lad
"""

import pandas as pd
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import RegexpStemmer
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import MWETokenizer
from nltk.tokenize import TweetTokenizer
from keras.preprocessing.text import text_to_word_sequence
from textblob import TextBlob
from nltk import ngrams
import re
sentence5 = "Sharad twitted ,wittnessing 70th republic day India from Rajpath,new delhi, Mesmorizing performance by Indian Army"
re.sub(r'(^\s\w]|_)+', '', sentence5).split()
# Extracting n-grams
# n-gram can be extracted using three techniques
# 1.custome defined function
# 2.NLTK
# 3.TextBlob
# 33
# Extracting n-grams using custom defined function


def n_gram_extractor(input_str, n):
    tokens = re.sub(r'(^\s\w]|_)+', '', input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])


n_gram_extractor("The cute little boy is playing with kitten", 2)
n_gram_extractor("The cute little boy is playing with kitten", 3)
#######################################
# exraction n-grams with nltk
list(ngrams("The cute little boy is playing with kitten".split(), 2))
list(ngrams("The cute little boy is playing with kitten".split(), 3))
#####################################
blob = TextBlob("The cute little boy is playing with kitten.")
blob.ngrams(n=2)
blob.ngrams(n=3)
######################################
# Tokenization using Keras,
sentence5
text_to_word_sequence(sentence5)
# 333
# Tokenization Using TextBlob
blob = TextBlob(sentence5)
blob.words
###########################################
# Tweet Tokenizer
tweet_tokenizer = TweetTokenizer()
tweet_tokenizer.tokenize(sentence5)
#########################
# Multi_word_Expression
sentence5
mwe_tokenizer = MWETokenizer([("republic", "day")])
mwe_tokenizer.tokenize(sentence5.split())
mwe_tokenizer.tokenize(sentence5.replace(';', ' ').split())
#########################################
# Regular Expression Tokenizer
reg_tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
reg_tokenizer.tokenize(sentence5)
################################################
# White space tokenizer
wh_tokenizer = WhitespaceTokenizer()
wh_tokenizer.tokenize(sentence5)
####################################
wp_tokenizer = WordPunctTokenizer()
wp_tokenizer.tokenize(sentence5)
#################################
sentence6 = "I love playing crickt.Cricket players practices hard in their inning"
regex_stemmer = RegexpStemmer('ing$')
' '.join(regex_stemmer.stem(wd) for wd in sentence6.split())
########################################
sentence7 = "Before eating, it would be nice to sanitize your hands with a sanitizer"
ps_stemmer = PorterStemmer()
words = sentence7.split()
" ".join([ps_stemmer.stem(wd) for wd in words])
######################################################
# Lemmatization
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
sentence8 = "The codes executed today are far better than what we execute generally"
words = word_tokenize(sentence8)
" ".join([lemmatizer.lemmatize(word) for word in words])
#########################################
###singularize and pluaralization
sentence9 = TextBlob("She sells seashells on the seashore")
words = sentence9.words
# we want to make word[2]i.e seashells in singular form
sentence9.words[2].singularize()
# 3we want word 5 i.e seashore in plural form
sentence9.words[5].pluralize()
######################################
# language translation from spanish to english
en_blob = TextBlob(u'muy bien')
en_blob.translate(from_lang='es', to='en')
# es:Spanish en:English
#####################################
# Custom stopwords removal
sentence9 = "She sells seashells on the seashore"
custom_stop_word_list = ['she', 'on', 'the', 'am', 'is']
words = word_tokenize(sentence9)
" ".join([word for word in words if word.lower()
          not in custom_stop_word_list])
# Select words which are not in defined list
###################################
# Extracting general features from raw text
# Number of words
# Detect presence of wh word
# Polarity
# Subjectivity
# Language identification
##################################
# To identify the number of words
df = pd.DataFrame([['The vaccine for covid-19 will be announced on 1st August '],
                  ['Do you know how much expectations the world population is having from this research?'], ['The risk of virus will come to an end on 31st July']])
df.columns = ['text']
df

# Now let us measure the number of words
df['number_of_words'] = df['text'].apply(lambda x: len(TextBlob(x).words))
df['number_of_words']

#############################
# Detect presence of words wh
wh_words = set(['why', 'who', 'which', 'what', 'where', 'when', 'how'])
df['is_wh_words_present'] = df['text'].apply(lambda x: True if len(
    set(TextBlob(str(x)).words).intersection(wh_words)) > 0 else False)
df['is_wh_words_present']

#################################
# Polarity of the sentence
df['polarity'] = df['text'].apply(
    lambda x: TextBlob(str(x)).sentiment.polarity)
df['polarity']
sentence10 = "I like this example very much"
pol = TextBlob(sentence10).sentiment.polarity
pol
sentence10 = "This is fantastic example and i like it very much"
pol = TextBlob(sentence10).sentiment.polarity
pol
sentence10 = "This was helpful example but i would have prefer another one"
pol = TextBlob(sentence10).sentiment.polarity
pol
########################################
# Subjectivity
df['subjectivity'] = df['text'].apply(
    lambda x: TextBlob(str(x)).sentiment.subjectivity)
df['subjectivity']
##########################################
# To find language of the sentence, this code will get http error
df['language'] = df['text'].apply(lambda x: TextBlob(str(x)).detect_language())
# IT is showing error here.
#####################################

# Bag of words
#This BoW converts unstructured  data to structured form
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus=['At least seven indian pharma companies are working to develope vaccine against the corona virus ',' The deadly virus that has already infected more than 14 million globally','Bharat Biotech is the among  the domastic phara firm workin on the corona virus vaccine in India']
bag_of_word_model=CountVectorizer()
print(bag_of_word_model.fit_transform(corpus).todense())
bag_of_word_df=pd.DataFrame(bag_of_word_model.fit_transform(corpus).todense())

#This will create dataFrame
bag_of_word_df.columns=sorted(bag_of_word_model.vocabulary_)
bag_of_word_df.head()
###########################################
#Bag of words model small
bag_of_word_model_small=CountVectorizer(max_features=5)
bag_of_word_df_small=pd.DataFrame(bag_of_word_model_small.fit_transform(corpus).todense())
bag_of_word_df_small.columns=sorted(bag_of_word_model_small.vocabulary_)
bag_of_word_df.head()

####################################################
##How To Use TF-IDF ##
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
corpus=['The mouse had a tiny little mouse','The cat saw the mouse','The cat catch the mouse','The end of the story']
#Step1 Initialize count vector
cv=CountVectorizer()
#To count the total no.of TF
word_count_vector=cv.fit_transform(corpus)
word_count_vector.shape
#Now next ste is to apply IDF
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)
#This matrix is in raw matrix form, let us convert it in DataFrame
df_idf=pd.DataFrame(tfidf_transformer.idf_,index=cv.get_feature_names_out(),columns=["idf_weights"])

#sort Ascending
df_idf.sort_values(by=['idf_weights'])

