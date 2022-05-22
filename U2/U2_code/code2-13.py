# -*- coding: utf-8 -*- 2-13  [     preprocessing.scale()  ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Sklearn Standardization 

from sklearn import preprocessing
import numpy as np
X = np.array([[ 1., -1., 2.], [ 2., 0., 0.],[ 0.,  1., -1.]])
# calculate mean
X_mean = X.mean(axis=0)
# calculate variance 
X_std = X.std(axis=0)
print(X)
print(X_mean)
print(X_std)
print("------------------------------------")
X_scaled = preprocessing.scale(X)
print(X_scaled)
print(X_scaled.mean(axis=0))
print(X_scaled.std(axis=0))
