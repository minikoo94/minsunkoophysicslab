#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


get_ipython().run_line_magic('matplotlib', 'inline')


#Create arrays for your data
theta = np.array ([50,47,43,41,38])
ymean = np.array ([84.88,84.6,84.32,87.48,88.325])

#Create an array for your y-axis uncertainties
yerr = np.array ([6.933801266,5.496544369,5.753398995,7.230048409,10.41260774])
#Reassign variables
x = theta
y = ymean
dy = yerr

#size the plot
plt.figure(figsize=(15,10))

#create scatter plot
plt.scatter(x, y, color='blue', marker='o')

#create labels
plt.xlabel('$\\theta$ (degrees)')
plt.ylabel('$y_{mean}$ (m)')
plt.title('Height on wall vs Launcher Angle')

#fitting to a 2nd degree polynomial
c,b,a=np.polynomial.polynomial.polyfit(x,y,2,w=dy)

#Annotate with values of A, B, C from best fit polynomial
plt.annotate('A = {value:.{digits}E}'.format(value=a, digits=3),
             (0.05, 0.9), xycoords='axes fraction')

plt.annotate('B = {value:.{digits}E}'.format(value=b, digits=3),
             (0.05, 0.85), xycoords='axes fraction')
             
plt.annotate('C = {value:.{digits}E}'.format(value=c, digits=3),
             (0.05, 0.8), xycoords='axes fraction')
#Create fit line
xnew = np.linspace(x.min(), x.max(), 300)
fit = a*xnew**2 + b*xnew +c

plt.scatter(xnew, fit, color='red')
plt.show()

print ("C = ",c , "B = ",b, "A = ",a)

