# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:16:29 2023

@author: HP
"""

#Aligning the text string
text = 'Hello World'
text.ljust(20)
#Out[20]: 'Hello World         '

text.rjust(20)
#Out[21]: '         Hello World'

text.center(20)
#Out[22]: '    Hello World     '
############################################33

#All of these methods accept an optional characters an fill character as well
text.rjust(20,'=')
#Out[23]: '=========Hello World'
text.center(20,'*')
#Out[24]: '****Hello World*****'
###################################################

format(text, '>20') #Text shifted on right side
#Out[25]: '         Hello World'

format(text, '<20') #text shifted on left side
#Out[26]: 'Hello World        '

format(text, '^20')  #Text is in middle    
#Out[27]: '    Hello World     '

format(text, '=>20s') #Empty space occupied by =
#Out[28]: '=========Hello World'

format(text, '*^20s')
#Out[29]: '****Hello World*****'

'{:>10s} {:>10s}'.format('Hello', 'World')
#Out[30]: '     Hello      World'

####################################################3

x = 1.2345
format(x, '>10')
x
#Out[7]: '    1.2345'

format(x, '^10.2f')
#Out[2]: '   1.23   '

##############################################
parts = ['IS','Chicago', 'Not', 'Chicago?']
' '.join(parts)
'Is Chicago Not Chicago?'
','.join(parts)
'Is,Chicago,Not,Chicago?'
''.join(parts)
'IsChicagoNotChicago?'#
#########################################
a = 'Is Chicago'
b = 'Not Chicago?'
a + ' ' + b
#Out[17]: 'Is Chicago Not Chicago?'
########################################

print('{} {}'.format(a,b))

#Is Chicago Not Chicago?
print(a + ' ' + b)
#Is Chicago Not Chicago?
############################################
a = 'Hello' 'world'
a
#Out[21]: 'Helloworld'
#######################
a = 'Hello'' ' 'world'
a
#Out[24]: 'Hello world'
#########################################################

