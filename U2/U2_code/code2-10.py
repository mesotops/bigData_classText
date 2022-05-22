# -*- coding: utf-8 -*-  2-10  [  Solution 3:  filling  data  by  SimpleImpute ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd 
import numpy as np 
from sklearn.impute import SimpleImputer
dict = {'A Score':[100, 90, np.nan, 95], 
        'B Score': [30, 45, 56, np.nan], 
        'C Score':[88, 40, 80, 98],
        'D Score':[70, 40, 80, 98],
        'E Score':[np.nan, 40, 80, 98],
        'F Score':[90, 40, 80, 98]} 
  
df = pd.DataFrame(dict)
print(df.isnull()) 
print("\n the number of A Score null value is :", df['A Score'].isnull().sum())
print("\n the number of C Score null value is :", df['C Score'].isnull().sum())
print(df)
print("\n ---------------------------------------------------------------")

"""
strategy : string, optional (default=”mean”)
mean  / median  / most_frequent  / “constant
"""
imp = SimpleImputer(missing_values=np.nan, strategy="median")
new_df = imp.fit_transform(df)
print(new_df)