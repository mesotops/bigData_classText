# -*- coding: utf-8 -*-   [    Code 4-2 : TransactionEncoder      ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from mlxtend.preprocessing import TransactionEncoder

transactions  = [['牛奶','麵包'], ['麵包','尿布','葡萄酒','甜菜'],
          ['牛奶','尿布','葡萄酒','橙汁'], ['麵包','牛奶','尿布','葡萄酒'],
          ['麵包','牛奶','尿布','橙汁']] 

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
print(te_ary)
print("")
print(te.columns_)      #list all of keywords(columns)