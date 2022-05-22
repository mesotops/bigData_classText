# -*- coding: utf-8 -*-  2-12  [  Solution 5:   interpolate  data  by  Pandas ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd 
import numpy as np 
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

###  method: { 'linear'   / time   /  index /  pad  /  nearest  / krogh / from_derivatives  }
###  limit_direction : {‘forward’, ‘backward’, ‘both’}, default ‘forward’
new_df = df.interpolate(method ='linear', limit_direction ='forward')
print(new_df)
