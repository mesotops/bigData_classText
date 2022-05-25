# -*- coding: utf-8 -*-   [     Code 6-12 :  Loading Data    ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
print(retail, "\n\n")

print(retail.shape, "\n\n")