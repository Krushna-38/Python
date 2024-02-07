# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 08:12:26 2023

@author: HP
"""

#Write a python code to plot two or more lines with legends, different width
import matplotlib.pyplot as plt
#line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
#line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
#set the x axis label of the current axis.
plt.xlabel('x - axis')
#set the y label of the current axis
plt.ylabel('y - axis')
#set a title
plt.title('Two or more lines withdifferent widths and colors with suitable')
#display the figure
plt.plot(x1,y1, color='blue', linewidth = 3, label = 'line1-width-3')
plt.plot(x2,y2, color='red', linewidth = 5, label = 'line2-width-5')
#Show a legend on the plot
plt.legend()
plt.show()
################################################
#Write a python program to plot 
import matplotlib.pyplot as plt
#line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
#line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
#set the x axis label of the current axis.
plt.xlabel('x - axis')
#set the y label of the current axis
plt.ylabel('y - axis')
#display the figure
plt.plot(x1,y1, color='blue', linewidth = 3, label = 'line1-dotted', linestyle='dotted')
plt.plot(x2,y2, color='red', linewidth = 5, label = 'line2-dashed', linestyle='dotted')
#set a title
plt.title("plot with two or more lines with different styles")
#Show a legend on the plot
plt.legend()
plt.show()

########################################################
#Write python program to plot two or more lines and set the line markers
import matplotlib.pyplot as plt
# xaxis value
x = [1,4,5,6,7]
# y axis values
y = [2,6,3,6,3]
#plottting points
plt.plot(x,y, color = 'red', linestyle = 'dashdot', linewidth = 3, marker='o', markerfacecolor= 'blue', markersize= 12)
#set the y-limits of the current axes.
plt.ylim(1,8)
#set the x-limits of the current axes.
plt.xlim(1,8)
#naming the x-axis 
plt.xlabel('x-axis')
#naming the y-axis
plt.ylabel('y-axis')
#set a title
plt.title('Display Marker')
#show a legend on the plot
plt.legend()
#To show the plot
plt.show()

############################################
#Write a python program to plot several lines with 
#different format styles in one command using array
import numpy as np
import matplotlib.pyplot as plt
#sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

#green dashesh, blue squares and red triangles
plt.plot(t ,t ,'g--', t, t**2, 'bs',t, t**3, 'r^')
plt.show()
#########################################
#Write a pythn program to display a bar chart of the 
#popularity of programming language
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity = [22.2,17.6,8.8,8,7.7,6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language\n"+"Worldwide, oct 2017 compared to a year ")
plt.xticks(x_pos, x)
plt.show()
############################################
#Write a pythn program to display a bar chart of the 
#popularity of programming language
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
popularity = [22.2,17.6,8.8,8,7.7,6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language\n"+"Worldwide, oct 2017 compared to a year ")
plt.yticks(x_pos, x)
plt.show()
##############################################
#Write a python 
import matplotlib.pyplot as plt
import numpy as np
# Data to plot
n_groups = 5
men_means =(22,30,33,30,26)
Women_means = (25,32,30,35,29)
#Create Plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
rects1 = plt.bar(index, men_means, bar_width, alpha=opacity, color='g', label='women')
plt.xlabel('Person')
color='r'
label='Women'
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index+bar_width, ('G1','G2','G3','G4','G5'))
plt.legend()
plt.tight_layout()
plt.show()


