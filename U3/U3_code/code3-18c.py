# -*- coding: utf-8 -*-   [3-18c ]   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#導入繪圖套件import numpy as np
import matplotlib.pyplot as plt


#設定座標範圍及座標數
fig = plt.figure(figsize=(15,5))
ax = fig.add_subplot(2, 2, 1)

# 設定座標範圍及座標數，將x座標範圍(set_xlim)設1~10.1，標籤(set_xticks)設定1~10，標籤間距為1
ax.set_xlim(1,10) ##設定x軸範圍
ax.set_xticks(range(1,11,1)) ##設定x軸標籤，set_xtick的範圍尾數要＋1
ax.set_ylim(-8,11)
ax.set_yticks(range(-8,11,2))
# 建立第2個子圖
ax2 = fig.add_subplot(2, 2, 2)
plt.show()
