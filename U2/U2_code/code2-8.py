# -*- coding: utf-8 -*-  2-8  [  Solution 1:  Drop data  by  Pandas ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd 
import numpy as np 
dict = {'A Score':[100, 90, np.nan, 95], 
        'B Score': [30, 45, 56, np.nan], 
        'C Score':[88, 40, 80, 98],
        'D Score':[70, 40, 80, 98],
        'E Score':[np.nan, 40, 80, 98],
        'F Score':[90, 40, 80, 98]} 
  
df = pd.DataFrame(dict)
print(df)
print("\n ---------------------------------------------------------------")
new_df=df.dropna() 
print(new_df)