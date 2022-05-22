# -*- coding: utf-8 -*-   [3-18d ]   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#導入繪圖套件import numpy as np
import matplotlib.pyplot as plt

#設定標籤顯示資料(set_xticklabels)，放入文字a~j，可以自行調整字體大小(fontsize)及旋轉角度(rotation)
#設定標籤顯示資料
fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim(1,10.1)
ax.set_xticks(range(1,11,1))
#設定x軸標籤文字，旋轉90度
ax.set_xticklabels(list("abcdefghij"),fontsize=20,rotation=90) 
ax.set_ylim(-8.5,11)
ax.set_yticks(range(-8,11,2))
ax.set_yticklabels(list("abcdefghij"),fontsize=30,rotation=45)
plt.show()