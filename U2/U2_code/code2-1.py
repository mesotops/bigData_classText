# -*- coding: utf-8 -*-  2-1 [    read.CSV    V1   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# reading csv file from internet 
import pandas as pd
df_iris = pd.read_csv('../Cust_Data Preprocessing.csv', header=None)

print("\n iris data:\n ", df_iris)
print("\n iris head: \n ", df_iris.head())
print("\n iris top 10 :\n ", df_iris.head(10))
print("\n iris describle: \n ", df_iris.describe())
