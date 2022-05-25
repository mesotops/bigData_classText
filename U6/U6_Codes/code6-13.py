# -*- coding: utf-8 -*-   [      Code 6-13 :  Exploratory Data Analysis - EDA      ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
# Import key Libraries
import pandas as pd
pd.set_option('display.max_columns', None)
# ~~~~~~~~~~~~~~~~~~~  [ Load data ] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Load data from Local Repository
# Data Source: http://archive.ics.uci.edu/ml/datasets/online+retail
raw = pd.read_excel('c:/Pyfiles/Online_Retail001.xlsx')  #  10000 samapling only by random()

# Create a copy to avoid re-loading the data due to the size of the file
# Work with "retail" dataframe and re-load from raw as required if needed
retail = raw

#  Review shape of Dataframe
print("No. of raws/columns = ", retail.shape, "\n\n")

# Inspect top 10 rows
print(" Top 5 data : \n", retail.head(), "\n\n")

# Inspect the dataset for missing values, datatypes & memory size
print("DataFrame information : \n ", retail.info(), "\n\n")


# View of NA rows across different features
print("No. of null values : \n", retail.isna().sum(), "\n\n")

# If we dropped any rows with NA, how many rows would we have left?
print("No. of drooped rows/Columns = ", retail.dropna().shape, "\n\n")

#Display object key information including Count, Unique values, Top value and frequency
print("Data Description : \n",  retail.describe(include=['object']), "\n\n")

#  Display statistics for numeric features including Count, Mean, Standard Deviation, Min, Max, etc...
print("Description Statistics : \n", retail.describe(), "\n\n")

# Number of records with negative quantity
print("No. of Quantity < 0 : ", retail.Quantity[retail.Quantity < 0 ].count(), "\n\n")

# Quick inspection of top records with Negative Quantity
print("Quantity < 0 : \n",  retail.loc[retail.Quantity < 0].head(10), "\n\n")

# Number of records with negative Unit Price 
print("No. of Unit Price < 0 = ", retail.UnitPrice[retail.UnitPrice < 0].count(),  "\n\n")

# Quick exploration of negative price records
print("Unit Price < 0 = ", retail.loc[retail.UnitPrice < 0], "\n\n")








