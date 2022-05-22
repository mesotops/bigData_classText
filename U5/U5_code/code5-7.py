# -*- coding: utf-8 -*-     [ Code 5-7 :   EDA :  Different Bar Charts    ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

# Figure 5: Bar Chart
fig, ax = plt.subplots(figsize=(18,15))
sns.barplot(x = 'loan', y = 'y', hue = 'day', data = df, ci=95, errwidth = 0.01)
plt.title('Mean success by current loan status for a given day of the month')
plt.show()

# Figure 6: 
fig, ax = plt.subplots(figsize=(18,15))
sns.barplot(x = 'job', y = 'y', hue = 'day', data = df, ci=95, errwidth = 0.01)
plt.xticks(rotation=45)
plt.title('Mean success by job title for a given day of the month')
plt.show()

# Figure 7: Crosstab 
pylab.rcParams['figure.figsize'] = (10, 8)
pd.crosstab(df.month, df.y).plot(kind='line')
plt.title('Purchase Frequency for Month')
plt.xlabel('Month')
plt.ylabel('Frequency of Purchase')
plt.show()
