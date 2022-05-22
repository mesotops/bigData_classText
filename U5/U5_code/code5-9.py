# -*- coding: utf-8 -*-    [  Code 5-9 :  DecisionTree Classifier : Accuracy Score +  Classification Report  + ROC   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import pandas as pd
import seaborn as sns
from matplotlib import pylab
from sklearn import tree
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn import metrics
from sklearn.metrics import f1_score, roc_curve, roc_auc_score, classification_report
from matplotlib import pyplot as plt

# pd.set_option('display.max_columns', None)

pylab.rcParams['figure.figsize'] = (3, 3)
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

# Load and read data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
df = pd.read_csv('c:/Pyfiles/bank.csv', sep= ';')
num_col = len(list(df.columns))
pd.set_option('display.max_columns', num_col * 3)

# EDA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("", df.head(), "\n\n")
# print("", df.describe().T, "\n\n")    # Transpose
# print("", df.groupby('y').mean().T, "\n\n")
# print("", df.groupby('job').mean().T, "\n\n")
# print("", df.groupby('marital').mean().T, "\n\n")
# print("", df.groupby('education').mean().T, "\n\n")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# lets get some more understanding of data and relationships
# print('check 1: ', df.groupby(['loan','y']).size())
# print('\n\ncheck 2: ', df.groupby(['job','y']).size())
# print('\n\ncheck 3: ', df.groupby(['marital','y']).size())
# print('\n\ncheck 4: ', df.groupby(['education','y']).size())
# print('\n\ncheck 5: ', df.groupby(['poutcome','y']).size())
# print('\n\ncheck 6: ', df.groupby(['month','y']).size())
# print('\n\ncheck 7: ', df.groupby(['y', 'default']).size())


#Label Encoding the class attribute
label_encoder = LabelEncoder()
label_encoder.fit(df["y"])
df["y"] = label_encoder.transform(df["y"])





# Feature Engineering ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
df['bal_sign'] = pd.Series(df['balance'] > 0)

labels = ['housing', 'default', 'loan']
for label in labels:
    label_encoder = LabelEncoder()
    label_encoder.fit(df[label])
    df[label] = label_encoder.transform(df[label])

# Will be On-Hot Encoded Later
cols = ['job', 'contact', 'marital','education', 'poutcome', 'month', 'day']
for label in cols:
    label_encoder = LabelEncoder()
    label_encoder.fit(df[label])
    df[label] = label_encoder.transform(df[label])


# From the above plot we can observe that most of the features are independent of each other.
# Feature-pair (pdays - previous) is highly negatively correlated.
# Therefore we can remove "pdays"
df = df.drop(["pdays"], axis = 1)
# df_corr = final_df.corr()



df = pd.get_dummies(df, columns = cols)
# print("", df.head(), "\n\n")
# print("", df.describe().T,"\n\n")

# Normalizing the Features ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
labels = df.y
scaler = MinMaxScaler()
features = pd.DataFrame(scaler.fit_transform(df.drop(['y'], axis = 1)), columns = df.drop(['y'], axis = 1).columns)
# print("", features.head(), "\n\n")

x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=1, stratify = labels)

cv = StratifiedKFold(n_splits = 5, shuffle=True, random_state = 1)

# DataFrame to store results


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ V 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creating a DecisionTree Classifier  

# clf = tree.DecisionTreeClassifier(criterion='entropy')
clf_gini = tree.DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=3, min_samples_leaf=5)

customer_clf = clf_gini.fit(x_train, y_train)     

# print("customer_clf    = ", customer_clf)

# predicater 
y_test_predicted = customer_clf.predict(x_test)
# print(y_test_predicted)

# Correct answer
# print(y_test)
# print(y_test_predicted)


# Convert 'yes' or 'no' to 1 or 0 
# yy_test = pd.Series(map(lambda x: dict(yes=1, no=0)[x], y_test.values.tolist()), y_test.index)
# my_map = {'no': 0, 'yes': 1}
# yy_test_predicted = np.vectorize(my_map.get)(y_test_predicted)

print("\n\nAccuracy Score: ", metrics.accuracy_score(y_test,y_test_predicted), "\n\n")
print("F1 Score: ", f1_score(y_test, clf_gini.predict(x_test)), "\n\n")
print("Classification Report: \n", classification_report(y_test, y_test_predicted), "\n\n")


dectree_roc_auc = roc_auc_score(y_test, y_test_predicted)
fpr, tpr, thresholds = roc_curve(y_test, clf_gini.predict_proba(x_test)[:,1])

# Figure 10: DecisionTreeClassifier ROC Diagrams 
plt.figure(figsize= (10,8))
plt.plot(fpr, tpr, label='Decision Tree (Area = %0.2f)' % dectree_roc_auc)
plt.plot([0,1],[0,1],'r--')
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.05])
plt.xlabel('Fasle Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristics')
plt.legend(loc="lower right")
plt.savefig('DEC_ROC')
plt.show()