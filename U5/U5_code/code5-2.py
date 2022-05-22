# -*- coding: utf-8 -*-  [  Code 5-2 :  DecisionTreeClassifier  + Figs   /   iris  Data   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
#
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree

# Prepare the data data
iris = datasets.load_iris()
x = iris.data
y = iris.target

# print(iris.feature_names)
print(x)
print(y)
# Fit the classifier with default hyper-parameters
clf = DecisionTreeClassifier(random_state=0)
model = clf.fit(x, y)

text_representation = tree.export_text(clf)
print(text_representation)

fig = plt.figure(figsize=(15,12))
tree.plot_tree(clf, 
              feature_names=iris.feature_names,  
              class_names=iris.target_names,
              filled=True)
fig.savefig("decistion_tree.png")