# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:02:08 2023

@author: HP
"""

from PyPDF2 import PdfFileReader
# Importing required modules
from PyPDF2 import PdfReader

#creating a pdf reader object
reader = PdfReader('C:/1-python/Quiz-3.pdf')
#Printing number of pages in pdf file
print(len(reader.pages))

#Getting a specific page from the pdf file
page = reader.pages[0]

#Extracting text from page
text = page.extract_text()
print(text)

################################################3333
import re
chat2 = 'Hi: I have problem with my order number 32323448'
pat = '\d{8}'
num=re.findall(pat,chat2)
num
###########################################################
#Pattern To find mobile number
import re
text1="My*mobile*number*is*9588453287"
text2="my*alternate*mobile*number*is*3212314843"
text3="My international mobile number is(124)-456-23231"
pat1='\d{10}'
mob_num=re.findall(pat1,text1)
mob_num
#To find international mobile number
pat2='\(\d{3}\)-\d{3}-\d{5}'
mob_num=re.findall(pat2,text3)
mob_num
#################################################

#Pattern to find E-mail id
import re
text1="My email-id is krushnalad@gmail.com"
text2="my*alternate email-id is krushna_lad@gmail.com"
text3="My official email-id is krushna321@gmail.com"
pat1 ='[a-z_A-z0-9]*@[a-z]*\.com'
email_id=re.findall(pat1,text3)
email_id
############################################
import re
text1="Krushna.Lad@sanjivani.org.in"
pat1='[a-z_A-Z]*.'
name=re.findall(pat1,text1)
name
#########################################333
#To get order number
import re
text1="Hi my order #455588 is not received yet"
text2="Hi I have problem with my order number 393320"
text3=" Hi my order 999403439 is having an issue"
pat1='order[^\d]*\d*'
order=re.findall(pat1,text3)
order
#########################################
#TO get only a number
import re
text1="Hi my order #455588 is not received yet"
text2="Hi I have problem with my order number 393320"
text3=" Hi my order 999403439 is having an issue"
pat2='order[^\d]*(\d*)'
order=re.findall(pat2,text1)
order
############################################

import re
chat1= 'Hello, I am having an issue with my order # 344434'
pattern= 'order[^\d{6}]*(\d{6})'
matches =re.findall(pattern,chat1)
matches

#####################################
#To find pattern match
import re
def get_pattern_match(pattern,text1):
    matches = re.findall(pattern,text1)
    if matches:
        return matches
get_pattern_match(r'order[^\d]*(\d)', chat1)

##########################################################3
#Retrieve email id and phone

text= '''   
Born Elon Reeve Musk
June 28, 1971 (age 51)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and chairman of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp. and X.AI
Co-founder of Neuralink, OpenAI, Zip2 and X.com (part of PayPal)
Spouses	
Justine Wilson
'''
get_pattern_match(r'age(\d+)',text)
match=get_pattern_match(r'Born(.*)',text)
match[0].strip()

match1=get_pattern_match(r'Born(.*)', text).lstrip()
match1
get_pattern_match(r'\(age.*\n(.*)', text)

####################################
def extract_personal_information(text):
    age= get_pattern_match(r'age(\d+)',text)
    full_name=get_pattern_match('Born(.*)\n',text)
    birth_date=get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place=get_pattern_match('\(age.*\n(.*)',text)
    return{
        }

#######################################

text1 = '''
Mukesh Dhirubhai Ambani was born on
 19 April 1957 in the British Crown colony
 of Aden (present-day Yemen) into a Gujarati Hindu
 family to Dhirubhai Ambani and Kokilaben Ambani.
 He has a younger brother Anil Ambani and two sisters,
 Nina Bhadrashyam Kothari and Dipti Dattaraj Salgaonkar.
 Ambani lived only briefly in Yemen because 
 his father decided to move back to India
 in 1958[8] to start a trading business that
 focused on spices and textiles. The latter w
 as originally named "Vimal" but later changed to
 "Only Vimal".[9][10] His family lived in a modest
 two-bedroom apartment in Bhuleshwar, Mumbai until
 the 1970s.[11] The family's financial status slightly 
 improved when they moved to India but Ambani still
 lived in a communal society, used public transportation,
 and never received an allowance.[12] 
 Dhirubhai later purchased a 14-floor apartment 
 block called 'Sea Wind' in Colaba, where, until 
 recently, Ambani and his brother lived with their 
 families on different floors.[13]
 '''
get_pattern_match(r'age(\d+)',text1)
match=get_pattern_match(r'Born(.*)',text1)
match[0].strip()

match1=get_pattern_match(r'Born(.*)', text1).lstrip()
match1
get_pattern_match(r'\(age.*\n(.*)', text1)

############################################################
#1. Extract all twitter handles from following text.
text='''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla

'''
pattern = 'https://twitter\.com/([a-zA-Z0-9_]+)'
re.findall(pattern,text)
###########################################################33
# Extract Concentration risk
text ='''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31,
'''
pattern = 'Concentration of Risk:([^\n]*)'
re.findall(pattern,text)
##############################################################3
#Companies in europe reports their financial numbers of semi annual basis

text = '''
Tesla's gross cost of operating lease 
vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles 
in FY2021 S1 was $8 billion.
'''
pattern = 'FY(\d{4} (?:Q[1-4]|s[1-2]))'
matches = re.findall(pattern, text)
matches
###############################################################
#Extract phone numbers

text='''
Elon musk's phone number is 9991116666, 
call him if you have any questions on dodgecoin. 
Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern = '\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches = re.findall(pattern, text)
matches

##########################################################
#Note
text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''
pattern = 'Note \d - ([^\n]*)'
matches = re.findall(pattern, text)
matches
#######################################################3
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern = 'FY\d{4} Q[1-4]'
matches =re.findall(pattern,text)
matches
###########################################################33
#Case sensitive pattern match using flags
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''
pattern = "FY\d{4} Q[1-4]"
matches = re.findall(pattern,text,flags=re.IGNORECASE)
matches
############################################################
#Extract only financial numbers
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern = '\$([0-9\.]+)'
matches = re.findall(pattern,text)
matches
