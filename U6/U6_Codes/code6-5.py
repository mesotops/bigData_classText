# -*- coding: utf-8 -*-   [     Code 6-5 :  BIRCH Clustering  (sklearn Dataset)   V1     ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn import datasets
from sklearn import metrics
from sklearn.cluster import Birch

# Prepare the data data
df_iris = datasets.load_iris()
iris_x = df_iris.data
iris_y = df_iris.target


brc = Birch(branching_factor=50, n_clusters=3, threshold=1)


print(iris_y)
print("-------------------------------------------")
brc.fit(iris_x)
brc_prd = brc.predict(iris_x)
print(brc_prd)
print("-------------------------------------------")
silhouette_avg = metrics.silhouette_score(iris_x, brc_prd)
print(silhouette_avg)

