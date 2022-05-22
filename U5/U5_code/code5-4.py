# -*- coding: utf-8 -*-   [  Code 5-4 :    Entropy     ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree

# Prepare the data data
iris = datasets.load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test =    train_test_split(x, y, 
                     test_size=0.3, 
                     random_state=0, 
                     stratify=y)

print("the size of X_train is : ", len(x_train))
print("the size of X_test  is : ", len(x_test))
print("the size of Y_train is : ", len(y_train))
print("the size of Y_test  is : ", len(y_test)) 


# Creating a classifier :  default = gini
clf = tree.DecisionTreeClassifier(criterion='entropy')
iris_clf = clf.fit(x_train, y_train)
print("iris_clf    = ",iris_clf, "\n\n")

# Prediction 
y_test_predicted = iris_clf.predict(x_test)
print(y_test_predicted)

# Answer 
print(y_test)
