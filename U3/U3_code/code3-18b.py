# -*- coding: utf-8 -*-   [3-18b ]   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#導入繪圖套件import numpy as np
import matplotlib.pyplot as plt
#建立初始圖框
fig = plt.figure(figsize=(15,5))
#在fig圖裡可以切塊 2X3 個子圖 顯示4個子圖
ax = fig.add_subplot(2, 3, 1)

ax2 = fig.add_subplot(2, 3, 2)
ax3 = fig.add_subplot(2, 3, 3)
ax4 = fig.add_subplot(2, 3, 5)
plt.show()
