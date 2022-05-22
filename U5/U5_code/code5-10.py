# -*- coding: utf-8 -*-    [  Code 5-10 : MLPClassifierr :  Accuracy Score +  Classification Report  + ROC   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import pandas as pd
from matplotlib import pylab
from sklearn import metrics
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score, roc_curve, roc_auc_score, classification_report
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from matplotlib import pyplot as plt
import seaborn as sns


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
