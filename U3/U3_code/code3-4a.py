#
# -*- coding: utf-8 -*-   [ 3-4a (Bar Charts)]    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import matplotlib.pyplot as plt
import numpy as np

x=['Mi','Samsung','Huawei','Apple','VIVO','OPPO']
y1=[46,95,134,127,101,75]
y2=[80,116,36,71,142,28]

width = 0.35
x1 = np.arange(len(x)) 

fig, ax = plt.subplots()
rects1 = ax.bar(x1 - width/2, y1, width)
rects2 = ax.bar(x1 + width/2, y2, width)

ax.set_title('Matplotlib—Bar Charts')
ax.set_xticks(x1)    # 設定刻度標籤字型大小
ax.set_xticklabels(x)    # 設定標籤顯示資料
ax.legend(["men", "women"], loc='upper left') 
plt.show()

#plt.xticks(fontsize= ) 設定刻度標籤字型大小
# ax.set_xticklabels(xlabels, fontsize= )
# plt.setp(ax.get_xticklabels(), fontsize=)
# ax.tick_params(axis='x', labelsize= ) 設定刻度標籤字型大小
# plt.legend(loc='lower left') // upper right, center right.......
