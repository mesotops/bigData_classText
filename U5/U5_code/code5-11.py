# -*- coding: utf-8 -*-   [ Code 5-11 : LogisticRegression  :  Accuracy Score +  Classification Report  + ROC   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import pandas as pd
from matplotlib import pylab
from sklearn import metrics
from sklearn.metrics import f1_score, roc_curve, roc_auc_score, classification_report
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from matplotlib import pyplot as plt
import seaborn as sns
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ V 3 : LogisticRegression ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# pd.set_option('display.max_columns', None)

pylab.rcParams['figure.figsize'] = (3, 3)
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

# Load and read data ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
df = pd.read_csv('c:/Pyfiles/bank.csv', sep= ';')
num_col = len(list(df.columns))
pd.set_option('display.max_columns', num_col * 3)

# EDA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print("", df.head(), "\n\n")

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
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=1, stratify = labels)
cv = StratifiedKFold(n_splits = 5, shuffle=True, random_state = 1)

# DataFrame to store results



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ V 3 : LogisticRegression ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

params = [
            {
                "penalty" : ['l2'], 
                "C" : [0.01, 0.1, 1.0, 10.0], 
                "solver" : ["sag"], 
                "max_iter" : [100, 200]
            },
            {
                "penalty" : ['l1'], 
                "C" : [0.01, 0.1, 1.0, 10.0], 
                "solver" : ["saga"], 
                "max_iter" : [100, 200]
            }
]
clf = GridSearchCV(estimator = LogisticRegression(n_jobs = -1, class_weight = "balanced"), param_grid = params, cv = cv, 
                   n_jobs = -1, scoring = "f1")
clf.fit(x_train, y_train)

y_test_predicted=clf.predict(x_test)
# print()
# print("The prediction result is:")
# print(y_test_predicted)

print("\n\nAccuracy Score: ", metrics.accuracy_score(y_test,y_test_predicted), "\n\n")
print("F1 Score: ", f1_score(y_test, clf.predict(x_test)), "\n\n")
print("Classification Report: \n", classification_report(y_test, y_test_predicted), "\n\n")


dectree_roc_auc = roc_auc_score(y_test, y_test_predicted)
fpr, tpr, thresholds = roc_curve(y_test, clf.predict_proba(x_test)[:,1])

# Figure 12: LogisticRegression  ROC Diagrams 
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
