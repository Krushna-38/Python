# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 09:08:30 2023

@author: HP
"""

#Whitespace stripping
s = ' hello world \n'
s.strip()
#'hello world'

s = ' hello world \n'
s.lstrip()
#'hello world \n'

s.rstrip()
s = ' hello world \n'
#' hello world'

#character stripping
t = '----hello===='
t.lstrip('-')
#'hello===='
t.strip('-=')
# 'hello'

s = ' hello world \n'
s = s.strip()
s
#'hello world'

s.replace(' ','')
#'hello world'

######################################
import re
re.sub('\s+', '', s)
'hello world'

################################
