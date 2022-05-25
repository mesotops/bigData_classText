# -*- coding: utf-8 -*-   [   Code 6-4a :  Hierarchial clustering   V1   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

samples = [[14, 15], [22, 28], [15, 18], [20, 30], [30, 35], [18, 20],
     [32, 30]]

res = linkage(samples, method='ward')
fig = plt.figure(figsize=(15, 10))
dendrogram(res,
           labels=samples,
           leaf_rotation=90,
           leaf_font_size=15,
           )

plt.show()


""""
method=’single’ 
method=’complete’
method=’average’
method=’weighted’
method=’centroid’
method=’median’ 
method=’ward’ 

X = [[2,2], [1,8], [0,7], [3,4], [1,3], [7,9], [6,9], [3,0]]
X = [[14,15], [22,28], [15,18], [20,30], [30,35], [18,20], [32,30]]"""