# -*- coding: utf-8 -*-   [   Code 6-2 :  Pearson correlation coefficient  V1   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import numpy as np

a_list = [2, 44, 12, 6, 77]
b_list = [2, 54, 13, 15, 55]
#b_list = [2, 44, 12, 6, 77]

a = np.array(a_list)
b = np.array(b_list)
print(np.corrcoef(a,b))