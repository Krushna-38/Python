# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 08:29:25 2023

@author: HP
"""

#write numpy program to compute 
import numpy as np
p = [[1,0],[0,1]]
q = [[1,2],[3,4]]
print("original matrix:")
print(p)
print(q)
result1 = np.dot(p,q)
print("Result of the said matrix multiplication:")
print(result1)

#Write a Numpy program to compute the outer product of two given vectors
import numpy as np
p = [[1,0],[0,1]]
q = [[1,2],[3,4]]
print("original matrix:")
print(p)
print(q)
result1 = np.outer(p,q)
print("outer product of the said vector:")
print(result1)

#Write numpy program to compute the cross product of two given vector
import numpy as np
p = [[1,0],[0,1]]
q = [[1,2],[3,4]]
print("original matrix:")
print(p)
print(q)
result1 = np.cross(p,q)
result2 = np.cross(q,p)
print("cross product of the said two vectors(p,q):")
print(result1)
print("cross product of the said two vectors(q,p)")
print(result2)

#Write the numpyprogram to compute the determinant
import numpy as np
from numpy import linalg as LA
a = np.array([[1,0],[1,2]])
print("Original 2-d array")
print(a)
print("Determinant of the said 2-D array:")
print(np.linalg.det(a))

#Wrtie a Numpy program to compute the eigenvalues and eienvecgtors
import numpy as np
m = np.mat("3 -2;1 0")
print("Original matrix:")
print("a\n", m)
w,v = np.linalg.eig(m)
print("Eigenvector of the said matrix",w)
print("Eigenvalues of the said matrix", v)
##################################################3

#write numpy program to compute inverse of a given  matrix
import numpy as np
m = np.array([[1,2],[3,4]])
print("Original matrix:")
print(m)
result = np.linalg.inv(m)
print("Inverse of the said matrix:")
print(result)
##################################################
#Write a Numpy program to generate five random numbers from the normal distribution
import numpy as np
x = np.random.normal(size=5)
print(x)
#####################################################
#Write nupy program to generate six random integes between 10 to 30
import numpy as np
x = np.random.randint(low = 10, high=30, size=6)
print(x)
####################################################
#Write numpy program to create a 3x3x3 array with random values
import numpy as np
x = np.random.random((3,3,3))
print(x)
###########################################
#Write numpy program to find 5x5 array with random values 
#and find the  minimum and maximum values
import numpy as np
x = np.random.random((5,5))
print("Original Array:")
print(x)
xmin, xmax = x.min(), x.max()
print("Minimum and Maximum Values:")
print(xmin, xmax)
#############################################
