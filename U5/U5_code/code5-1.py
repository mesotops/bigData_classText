# -*- coding: utf-8 -*-   [  Code 5-1 :   UCI  iris Data     ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import numpy as np
import pandas as pd
# from sklearn.cross_validation import train_test_split

df_iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
df_iris.columns = ["SepalLengthCm",	"SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]
print('----------------------------------------------------------------------\n')
print('Species', np.unique(df_iris['Species']))
print('----------------------------------------------------------------------\n')
#  print(df_iris.head())
print(df_iris)
