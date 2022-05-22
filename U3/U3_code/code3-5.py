#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -*- coding: utf-8 -*-   [ 3-5. (Bar Charts)]    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import numpy as np
import matplotlib.pyplot as plt

bar_value = np.random.random(5)
x_position = np.arange(5)+1

plt.barh(x_position,bar_value,height=0.3,color = 'r')
plt.xlabel('Bar Charts')