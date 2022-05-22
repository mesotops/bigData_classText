# -*- coding: utf-8 -*- 2-18  [     RobustScaler  ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#     [-1, 1]
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import RobustScaler

url_iris = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ["SepalLengthCm",	"SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]
df_iris = pd.read_csv(url_iris, names=columns) 
array = df_iris.values 
print(df_iris.head())
# separate array into input and output components 
X = array[:,0:4] 
Y = array[:,4] 

scaler = RobustScaler().fit(X) 
rescaledX = scaler.transform(X) 
  
# summarize transformed data 
np.set_printoptions(precision=3) 
print(rescaledX[0:5,:]) 