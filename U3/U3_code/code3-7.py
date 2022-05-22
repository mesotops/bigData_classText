# -*- coding: utf-8 -*-   [ 3-7.柱狀圖 (Bar Charts) ]    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})
# Create Data
x=['A','B','C','D','E','F','G','H','I','J']
y = np.random.randint(low=0, high=100, size=10)
y
array=[47, 23, 27,  0, 82,  7, 46, 92, 36, 76]

# Horizontal Bar plot
plt.barh(x,y)
plt.xlabel("Values")
plt.ylabel('Categories')
plt.title('Horizontal Bar Plot')
plt.show()