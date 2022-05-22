# -*- coding: utf-8 -*-  2-6  [    notnull    V1  ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import pandas as pd 
import numpy as np 
dict = {'A Score':[100, 90, np.nan, 95], 
        'B Score': [30, 45, 56, np.nan], 
        'C Score':[88, 40, 80, 98],
        'D Score':[70, 40, 80, 98],
        'E Score':[np.nan, 40, 80, 98],
        'F Score':[90, 40, 80, 98]} 
 
df = pd.DataFrame(dict)
print(df.notnull()) 
print("\n the number of A Score null value is :", df['A Score'].isnull().sum())
print("\n the number of C Score null value is :", df['C Score'].isnull().sum())