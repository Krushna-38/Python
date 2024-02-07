# -*- coding: utf-8 -*-
"""
Created on Thu May 25 21:33:08 2023

@author: HP
"""

import pandas as pd
df = pd.read_csv('Attendance.csv')
df

#Rename name column
df2=df.rename({'parjane pranjal':'pranjal'},axis='columns')
df2
#######################################