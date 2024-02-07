# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:57:32 2023

@author: Krushna Lad
"""
from bs4 import BeautifulSoup as bs
import requests
link='https://www.flipkart.com/poco-m6-pro-5g-power-black-128-gb/p/itmef8fa46f89738?pid=MOBGRNZ3ER4N3K4F&lid=LSTMOBGRNZ3ER4N3K4FIYYGCU&marketplace=FLIPKART&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=b_1_1&otracker=browse&fm=organic&iid=e00fcd36-3a73-4acf-97e2-4e8c7e409be3.MOBGRNZ3ER4N3K4F.SEARCH&ppt=browse&ppn=browse&ssid=y0gyo27oeo0000001699243363410'
page=requests.get(link)
page
page.content
soup=bs(page.content,'html.parser')
print(soup.prettify())
title=soup.find_all('p',class_="_2-N8zT")
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
len(review_title)

#We got 10 review titles
#Now let us scrap rating
rating=soup.find_all('div',class_='_3LWZLK _1BLPMq')
rating
rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
len(rate)
rate.append('')
rate.append('')
rate.append('')
len(rate)
################################
#Now let us scrap the review body
review=soup.find_all('div',class_='t-ZTKy')
review 
review_body=[]
for i in range(0,len(review)):
    review_body.append(review[i].get_text())
review_body
len(review_body)
##We got 10 review_body
##Now we have to save the data in .csv file
import pandas as pd
df=pd.DataFrame()
df['Review_Title']=review_title
df['Rate']=rate
df['Review']=review_body
df
#####################33333333
##To create .csv file
df.to_csv("C:/Dataset/flipkart_review.csv",index=True)
##################
#Sentiment analysis
import pandas as pd
from textblob import TextBlob
sent="This is very excellent garden"
pol=TextBlob(sent).sentiment.polarity
pol
df=pd.read_csv()
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
