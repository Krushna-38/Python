# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:37:48 2023

@author: HP
"""
list_a = [1,2,3,4,5]
list_b = list_a
list_a[0] = [-10]
print(list_a)
print(list_b)
###########################################333
import copy 
list_a =[1,2,3,4,5]
list_b = copy.copy(list_a)
list_b[0] = -10
print(list_a)
print(list_b)
#[1, 2, 3, 4, 5]
#[-10, 2, 3, 4, 5]
##########################################3333
import copy
list_a = [[1,2,3,4,5],[6,7,8,9,10]]
list_b = copy.copy(list_a)
list_a[0][0] = -10
print(list_a)
print(list_b)
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
################################################
import copy
list_a = [[1,2,3,4,5],[6,7,8,9,10]]
list_b = copy.deepcopy(list_a)
list_a[0][0]=-10
print(list_a)
print(list_b)
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
###############################################
