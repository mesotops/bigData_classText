# -*- coding: utf-8 -*-  2-3  [     Iris data for descriptive statistics     ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import numpy as np
from scipy import stats
import statistics as stat

df_iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

#  ~~~~~~~~~~~~~~~  statistics version ~~~~~~~~~~~~~~~~~~~~~

meanS = stat.mean(df_iris[1])
print("stat 平均數 : ", meanS)
print("------------------------------------\n")
modelS = stat.mode(df_iris[1])
print("stat 眾數 : ", modelS)
print("------------------------------------\n")
medianS = stat.median(df_iris[1])
print("stat 中位數 : ", medianS)
print("------------------------------------\n")
stdevS = stat.stdev(df_iris[1])
print("stat 標準差 : ", stdevS)
print("------------------------------------\n")
varianceS = stat.variance(df_iris[1])
print("stat 變異數 : ", varianceS)
print("------------------------------------\n")
print("------------------------------------\n")


#  ~~~~~~~~~~~~~~~  np version ~~~~~~~~~~~~~~~~~~~~~

meanN = np.mean(df_iris[1])
print("Numpy 平均數 : ",meanN)
print("------------------------------------\n")
modelN = stats.mode(df_iris[1])
print("scipy 眾數 : ", modelN)
print("------------------------------------\n")
medianN = np.median(df_iris[1])
print("numpy 中位數 : ", medianN)
print("------------------------------------\n")
stdevN = np.std(df_iris[1])
print("numpy 標準差 : ", stdevN)
print("------------------------------------\n")
varianceN = np.var(df_iris[1])
print("numpy 變異數 : ", varianceN)
print("------------------------------------\n")
varianceN2 =(meanN/stdevN)
print("numpy 變異數 2: ", varianceN2)
print("------------------------------------\n")
