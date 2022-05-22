# -*- coding: utf-8 -*-  06  [  Code 5-6 :  EDA : Count / Histogram Diagrams    ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib import pylab



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


# Exploratory Visualization  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Figure 1: Yes/No ratio Bar
fig, ax = plt.subplots(figsize=(8,5))
ratio = df.y[df.y == "yes"].count() / df.y.shape[0]
print('Ratio of classes (no : yes)', 1- ratio, ':', ratio)
sns.countplot(df.y)
plt.show()

# Figure 2: Age Histogram 
fig, ax = plt.subplots(figsize=(8,5))
df.age.hist()
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Figure 3: marital Diagrams 
fig, ax = plt.subplots(figsize=(8,5))
sns.countplot(y = df.marital, data = df)
plt.show()

# Figure 4: Job Count Diagrams
fig, ax = plt.subplots(figsize=(8,5))
sns.countplot(y = df.job, data = df)
plt.show()