# -*- coding: utf-8 -*-   [   Code 6-7 :   KMeans   by  Random  ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from matplotlib import pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans

X, y = make_blobs(n_samples=500, centers=5, cluster_std=0.60, random_state=0)
plt.scatter(X[:,0], X[:,1])

wcss = []     #   損失函數 WCSS (within-cluster sum of squares)  組內平方和
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(X)
plt.scatter(X[:,0], X[:,1])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
plt.show()

"""
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

[parameters:]
n_clusters: int, default=8
init: {‘k-means++’, ‘random’, ndarray, callable}, default=’k-means++’
n_init: int, default=10
max_iter: int, default=300
tol: float, default=1e-4
random_state: int, RandomState instance, default=None
algorithm: {“auto”, “full”, “elkan”}, default=”auto”

[Attributes:] 
cluster_centers_: ndarray of shape (n_clusters, n_features)
           Coordinates of cluster centers. If the algorithm stops before fully converging (see tol and max_iter), these will not be consistent with labels_.
labels_: ndarray of shape (n_samples,)
           Labels of each point
inertia_: float
     Sum of squared distances of samples to their closest cluster center.

n_iter_: int
      Number of iterations run.

參數的意義：
n_clusters: 聚類的個數
init: 初始聚類中心的獲取方法
n_init: 獲取初始聚類中心的更叠次數，為了彌補初始質心的影響，算法默認會初始10次質心，實現算法，然後返回最好的結果。
max_iter: 最大叠代次數（因為kmeans算法的實現需要叠代）
tol: 容忍度，即kmeans運行準則收斂的條件
precompute_distances：是否需要提前計算距離，這個參數會在空間和時間之間做權衡，如果是True 會把整個距離矩陣都放到內存中，auto 會默認在數據樣本大於featurs*samples 的數量大於12e6 的時候False,False 時核心實現的方法是利用Cpython 來實現的
verbose: 冗長模式（不太懂是啥意思，反正一般不去改默認值）
random_state: 隨機生成簇中心的狀態條件。
copy_x: 對是否修改數據的一個標記，如果True，即復制了就不會修改數據。bool 在scikit-learn 很多接口中都會有這個參數的，就是是否對輸入數據繼續copy 操作，以便不修改用戶的輸入數據。這個要理解Python 的內存機制才會比較清楚。
n_jobs: 並行設置
algorithm: kmeans的實現算法，有：’auto’, ‘full’, ‘elkan’, 其中 ‘full’表示用EM方式實現
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
"""
