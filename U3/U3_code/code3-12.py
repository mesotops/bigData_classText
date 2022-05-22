# -*- coding: utf-8 -*-   [範例  3-12.散佈圖 (Scatter Chart) ]    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import numpy as np 
from matplotlib import pyplot as plt 

x = np.arange(30)
y = x + 3*np.random.randn(30)
plt.scatter(x, y)

# random.randn函式 :  返回一個或一組樣本，具有標準常態分配。
# random.rand函式 : 根據給定維度生成[0,1)之間的資料，包含0，不包含1
# random.randint函式 : 返回隨機整數，範圍區間為[low,high），包含low，不包含high
# random.random_sample(size=None)
# random.random(size=None)
# random.ranf(size=None)
# random.sample(size=None)