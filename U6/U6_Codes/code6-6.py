# -*- coding: utf-8 -*-   [  Code 6-6 :     KMeans   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print(kmeans)
print(kmeans.labels_)
k_pred = kmeans.predict([[0, 0], [4, 4]])
print(k_pred)
print(kmeans.cluster_centers_)