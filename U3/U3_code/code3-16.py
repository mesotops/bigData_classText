# -*- coding: utf-8 -*-   [範例 3-16.圓餅圖 (Pie Chart) ]    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import matplotlib.pyplot as plt
labels = 'A','B','C','D','E','F'
size = [50,40,30,15,20,60]
separated = (.1,0,0,0,0,0)
plt.pie(size , labels = labels,autopct='%1.1f%%',explode=separated)
plt.axis('equal')
plt.show()
