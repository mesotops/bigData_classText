# -*- coding: utf-8 -*-   [範例 3-10.直方圖 (Histogram)]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import numpy as np 
from matplotlib import pyplot as plt 

a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
hist,bins = np.histogram(a,bins =  [0,20,40,60,80,100])  

plt.hist(a, bins) 
plt.title("histogram") 
plt.show()
