# -*- coding: utf-8 -*-   [   Code 6-8a :   KMeans  for  Iris   v1  ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

wcss =[]
for i in range(1, 11):
  kmeans = KMeans(n_clusters = i).fit(X)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)


plt.plot(range(1, 11), wcss, 'bx-')
plt.title('Elbow method')
plt.xlabel('No of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans3 = KMeans(n_clusters=3)
y_kmeans3 = kmeans3.fit_predict(X)
print(y)
print(y_kmeans3)
print(kmeans3.cluster_centers_)
plt.scatter(X[:,0], X[:,1], c=y_kmeans3, cmap='rainbow')