# -*- coding: utf-8 -*-   [    Code 4-4 : TransactionEncoder + DataFrame + Inverse    ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

transactions  = [['牛奶','麵包'], ['麵包','尿布','葡萄酒','甜菜'],
          ['牛奶','尿布','葡萄酒','橙汁'], ['麵包','牛奶','尿布','葡萄酒'],
          ['麵包','牛奶','尿布','橙汁']] 

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_trans = pd.DataFrame(te_ary, columns=te.columns_)
print(df_trans)
print("")
print(" ~~~~~~~~~~~~~~~ 資料還原及重排  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
org_trans = te_ary[:5]
print(te.inverse_transform(org_trans))
