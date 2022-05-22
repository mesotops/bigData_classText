# -*- coding: utf-8 -*- 2-2  [      read.CSV    V2      ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# reading csv file from internet with different formats
import pandas as pd 
url_iris = '../Cust_Data Preprocessing.csv'
columns = ["SepalLengthCm",	"SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]
df_iris = pd.read_csv(url_iris, names=columns) 

print("\n iris data:\n ", df_iris)
print("\n iris head: \n ", df_iris.head())
print("\n iris top 10 :\n ", df_iris.head(10))
print("\n iris describle: \n ", df_iris.describe())