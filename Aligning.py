# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 09:19:18 2023

@author: HP
"""

text = 'Hello world'
text.ljust(20)
#'Hello world         '

text.rjust(20)
#'         Hello world'

text.center(20)
# '    Hello world     '
############################################################
#All  of these methods accept an optional characters and fill
text.rjust(20,'=')
#'=========Hello world'

text.center(20,'*')
#'****Hello world*****'

####################################3
format(text, '>20')
#'         Hello world'

format(text,'<20')
#'Hello world         '

format(text,'^20')
#'    Hello world     '

#Here you can add characters to fill the space at left
format(text,'=>20s')
# '=========Hello world'

format(text, '*^20s')
#'****Hello world*****'

'{:>10s}{:>10s}'.format('Hello','world')
#'     Hello     world'
########################3333
x = 1.23345
format(x, '>10')
x
#'   1.23345'
format(x,'^10.2f')
#'   1.23   '
#######################################################

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)
#'Is Chicago Not Chicago?'
','.join(parts)
#'Is,Chicago,Not,Chicago?'
''.join(parts)
#'IsChicagoNotChicago?'