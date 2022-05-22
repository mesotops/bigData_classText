# -*- coding: utf-8 -*-   [ Code 5-5 : DecisionTreeClassifier   Gini   vs   Entropy ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
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


# Decision Tree Classifier with criterion gini index
clf_gini = tree.DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=3, min_samples_leaf=5)

print("gini   =  ", clf_gini)
clf_gini.fit(x_train, y_train)

# Decision Tree Classifier with criterion information gain
print("\n")
clf_entropy = tree.DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=3, min_samples_leaf=5)

print("entropy  = ", clf_entropy)
clf_entropy.fit(x_train, y_train)

print('-------------------------------------------------------------------------------\n')
print("correct answer is ", y_test, "\n")

# Prediction for Decision Tree classifier with criterion as gini index
y_pred = clf_gini.predict(x_test)
print("y_predication for gini is ", y_pred, "\n")

y_pred_en = clf_entropy.predict(x_test)
print("y_predication for entropy is ", y_pred_en, "\n")

print('-------------------------------------------------------------------------------\n')

#  Calculating Accuracy Score
# Accuracy for Decision Tree classifier with criterion as gini index
print("Accuracy for gini is ", accuracy_score(y_test,y_pred)*100, "%")

# Accuracy for Decision Tree classifier with criterion as information gain
print("Accuracy for entropy is ", accuracy_score(y_test,y_pred_en)*100, "%")