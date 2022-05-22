
#pip install mlxtend 
# -*- coding: utf-8 -*-   [   Installing apriori module   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#pip install apyori
# -*- coding: utf-8 -*-   [   Installing fp_growth module   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# -*- coding: utf-8 -*-   [    Code 4-1 : TransactionEncoder      ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from mlxtend.preprocessing import TransactionEncoder

transactions  = [['牛奶','麵包'], ['麵包','尿布','葡萄酒','甜菜'],
          ['牛奶','尿布','葡萄酒','橙汁'], ['麵包','牛奶','尿布','葡萄酒'],
          ['麵包','牛奶','尿布','橙汁']] 

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
print(te_ary)