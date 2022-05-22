# -*- coding: utf-8 -*-   [    Code 4-5 :  mlxtend: Apriori  + Frequent_itemsets      ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

transactions  = [['牛奶','麵包'], ['麵包','尿布','葡萄酒','甜菜'],
          ['牛奶','尿布','葡萄酒','橙汁'], ['麵包','牛奶','尿布','葡萄酒'],
          ['麵包','牛奶','尿布','橙汁']] 

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_trans = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df_trans, min_support=0.6, use_colnames=True)
print(frequent_itemsets)