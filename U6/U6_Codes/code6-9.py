# -*- coding: utf-8 -*-   [   Code 6-9 :    KMeans  for  Iris    ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from sklearn.cluster import KMeans
from sklearn import datasets, metrics
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

kmeans_fit = KMeans(n_clusters = 3, random_state=0).fit(X)
k_labels = kmeans_fit.labels_
print(" Clustering results -------------------------------------")
print(k_labels)
print(" Real Results -------------------------------------")
print(y)
silhouette_avg = metrics.silhouette_score(X, k_labels)
print("-------------------------------------")
print("silhouette_avg = ", silhouette_avg)
