# -*- coding: utf-8 -*- [  Code 4-10 :  mlxtend : fpgrowth +  Association_rules  +  CSV/Excel Output  + Filtering ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#import the library
#
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules
pd.set_option('display.max_columns', None)

#load the data
store_data = pd.read_csv('c:/Pyfiles/retail_dataset.csv')

#initialize a empty list
records = []
for i in range(0, 315):
  records.append([str(store_data.values[i,j]) for j in range(0, 7)])

for i,j in enumerate(records):
  while "nan" in records[i]: records[i].remove("nan")    
# print(records)

te = TransactionEncoder()
te_ary = te.fit(records).transform(records)
df_trans = pd.DataFrame(te_ary, columns=te.columns_)
#applying fpgrowth for frequent_itemsets
frequent_itemsets = fpgrowth(df_trans, min_support=0.2, use_colnames=True )

#antecedent support    consequent support   support   confidence  lift  leverage  conviction
association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.5)

#make it as a data frame
df_rules = pd.DataFrame(rules)
df_rules.to_excel('c:/Pyfiles/rule_retail.xlsx')
print(df_rules)
