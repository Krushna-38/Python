# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:25:34 2023

@author: HP
"""

########Text Mining ################
sentence="we are learning TextMining from Sanjivani AI"
### if we want to know position of learning
sentence.index("learning")
##IT will show learning is at position 7
##This is going to show character position from 0 
################################################33333
#We want to know position of textMining Word
sentence.split().index("TextMining")
###It will split the words in list and count the position
## If you want to see the list select sentence.split()
#And it will show at 3
######################################################3
#Suppose we want print any word in reverse order
sentence.split()[2][::-1]
###[start:end end:-1(start)] will start from 
#-1,-2,-3 till the end
##learning will be printed as gninrael
###########################################

#Suppose want to print first and last word of the sentence
words=sentence.split()
first_word=words[0]
first_word
last_word=words[-1]
last_word
##Now we want to concate the first and last word
concat_word=first_word+" "+last_word
concat_word
######################################
#We want to print even words from the sentences
[words[i] for i in range(len(words)) if i%2==0]
##Words having odd length will not be printed
#####################################################
sentence
#Now we want to display only AI
sentence[-3:]
###############################
#Suppose we want to diplay entire sentence in reverse order
sentence[::-1]
#IA inavijnas morf gniniMtxeT gninrael era ew
##################################
#Suppose we want to select each word and print in reversed order
words
print(" ".join(word[::-1]for word in words))
###ew era gninrael gniniMtxeT morf inavijnaS IA
###############################

#Tokenization
import nltk
nltk.download('punkt')
from nltk import  word_tokenize
words=word_tokenize("I am reading NLP Fundamentals")
print(words)

####################################################

#Parts of speech (POs) tagging
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)
#IT is going mention parts of speech
##############################################################
#Stop words from NLTK library
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words=stopwords.words('English')
##You can verify 179 stop words in variable explorer
print(stop_words)
sentence1="I am learning NLP:It is one of most popular library in python"
#Frist we will tokenize the sentence
sentence_words=word_tokenize(sentence1)
print(sentence_words)
#Now let us filter the sentence using stop_words
sentence_no_stops=" ".join([words for words in sentence_words])
print(sentence_no_stops)
sentence1
##You can notice that am,is,of,the most,popular,in are missing
###############################
#Suppose we want to replace words in string
sentence2="I visited MY from IND on 14-02-19"
normalized_sentence=sentence2.replace("MY","Malaysia").replace("IND","India").replace("-20","India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)
######################################################
#Suppose we want auto correction in the sentence
from autocorrect import Speller
#declare the function Speller defined for English
spell=Speller(lang='en')
spell("English")
########################33333###############
#Suppose we want to correct whole sentence
sentence3="Ntural Lanagage processin deals with the aart of extracting sentiiiments"
##Let us first toenize this sentence
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word) for word in sentence3])
print(corrected_sentence)

###################################################

##Stemming##
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programmed")
stemmer.stem("jumping")
stemmer.stem("jumped")
###############################################

##Lematizer##
#Lematizer looks into dictionary words
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programed")
lemmatizer.lemmatize("programs")

lemmatizer.lemmatize("battling")

lemmatizer.lemmatize("amazing")
######################################
##Chunking (Shallow Parsing) Identifying named entities
nltk.download("maxent_ne_chunker")
nltk.download("averaged_perceptron_tagger")
nltk.download("words")
sentence4="we are learning NLP in python by SanjivaniAI based in India"
###First we will tokenize
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]
##############################
##sentence Tokenization
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("we are learning NLP in python. Delevered by sanjivaniAI")
sent
####################################
from nltk.wsd import lesk
sentence1="keep your savings in the bank"
print(lesk(word_tokenize(sentence1),'bank'))
###Output Synset('Savings_bank.n.02')
sentence2="It is so risky to drive over the banks of river"
print(lesk(word_tokenize(sentence2),'bank'))
##Synset('bank.v.07')
##########
#sysnet('bank.n.07) a slope in the turn of a road or track;
#The outside is higher than the inside in order to reduce the
###
#"bank" as multiple meanings. if you want to find exact meaning
#Execute the following code
#The definitions for "bank" can be seen here:
from nltk.corpus import wordnet as wn
for
