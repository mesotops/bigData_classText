# -*- coding: utf-8 -*-  2-5b  [    isnull    V1   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# is null for the columns
import pandas as pd
df_iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
df_iris.columns = ["SepalLengthCm",	"SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]
print(df_iris.head())
print(df_iris['SepalLengthCm'].isnull())
print(df_iris['SepalLengthCm'].isnull().sum())
