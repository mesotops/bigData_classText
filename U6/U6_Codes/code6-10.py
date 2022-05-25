# -*- coding: utf-8 -*-   [   Code 6-10 : KMeans  FIG for  Iris (n=2~10)  v4  ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from sklearn import datasets, metrics
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

silhouette_avg = []
for i in range(2,11):
    kmeans_fit = KMeans(n_clusters = i).fit(X)
    silhouette_avg.append(metrics.silhouette_score(X, kmeans_fit.labels_))



# plt.plot(range(1,11), silhouette_avg)


plt.plot(range(2, 11), silhouette_avg, 'bx-')
plt.title('silhouette')
plt.xlabel('No of clusters')
plt.ylabel('Avg')
plt.show()

