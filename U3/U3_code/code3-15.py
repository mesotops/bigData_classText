# -*- coding: utf-8 -*-   [範例 3-15.圓餅圖 (Pie Chart)]   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import matplotlib.pyplot as plt
labels = 'A','B','C','D','E','F'
size = [15,20,30,15,8,12]
plt.pie(size , labels = labels,autopct='%1.1f%%')
plt.axis('equal')
plt.show()
# plt.pie(size,                           # 數值
#        labels = labels,                # 標籤
#        autopct = "%1.1f%%",            # 將數值百分比並留到小數點一位
#        explode = separeted,            # 設定分隔的區塊位置
#        pctdistance = 0.6,              # 數字距圓心的距離
#        textprops = {"fontsize" : 12},  # 文字大小
#        shadow=True)                    # 設定陰影
