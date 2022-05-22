# -*- coding: utf-8 -*-   [ 3-6.柱狀圖 (Bar Charts) ]    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import numpy as np
import matplotlib.pyplot as plt
# Figure size = 10X7, dpi= 100 
plt.rcParams.update({'figure.figsize':(10,7), 'figure.dpi':100})
# Create Data
x=['A','B','C','D','E','F','G','H','I','J']
y = np.random.randint(low=0, high=100, size=10)
y
array=[47, 23, 27,  0, 82,  7, 46, 92, 36, 76]

# Simple Bar Plot
plt.bar(x,y)
plt.xlabel('Categories')
plt.ylabel("Values")
plt.title('Categories Bar Plot')
plt.show()