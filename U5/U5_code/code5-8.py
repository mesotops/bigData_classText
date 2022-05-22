# -*- coding: utf-8 -*-    [ Code 5-8 :   EDA:  Correlation Tables ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib import pylab
from sklearn.preprocessing import LabelEncoder


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

#  Figure 8: A Correlation Table Before dropping columns 
df_corr = df.corr()
plt.figure(figsize=(18, 18))
sns.heatmap(df_corr, annot = True)
plt.show()


# From the above plot we can observe that most of the features are independent of each other.
# Feature-pair (pdays - previous) is highly negatively correlated.
# Therefore we can remove "pdays"
final_df = df.drop(["pdays"], axis = 1)
df_corr = final_df.corr()

#  Figure 9: A Correlation Table After dropping columns 
plt.figure(figsize=(18, 18))
sns.heatmap(df_corr, annot = True)
plt.show()
