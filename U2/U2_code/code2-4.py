# -*- coding: utf-8 -*- 2-4  [     Iris data for descriptive statistics  with matplotlib   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import numpy as np
from scipy import stats
import statistics as stat
from matplotlib import pyplot

df_iris = pd.read_csv('../Cust_Data Preprocessing.csv', header=None)

df_iris = df_iris.dropna()

pyplot.hist(df_iris[1])   # 直方圖
pyplot.show()
pyplot.hist(df_iris[1], 100, histtype='step', cumulative=True)   #累積曲線 
pyplot.show() 
pyplot.bar(df_iris[0], df_iris[1])  # 柱狀圖
pyplot.show()          
pyplot.scatter(df_iris[0], df_iris[2])  # 散點圖 
pyplot.show()
pyplot.boxplot(df_iris[1])  # 箱形圖  boxplot()
pyplot.show()
