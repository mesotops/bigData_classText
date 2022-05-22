# -*- coding: utf-8 -*-   [    Code 4-7 :  mlxtend:  Apriori   + Association_rules       ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
transactions  = [['牛奶','麵包'], ['麵包','尿布','葡萄酒','甜菜'],
          ['牛奶','尿布','葡萄酒','橙汁'], ['麵包','牛奶','尿布','葡萄酒'],
          ['麵包','牛奶','尿布','橙汁']] 

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_trans = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df_trans, min_support=0.6, use_colnames=True)
frequent_itemsets['item_length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x)) 
print(frequent_itemsets)
print("")
print("")
print(association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7))
