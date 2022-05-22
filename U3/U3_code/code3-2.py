# -*- coding: utf-8 -*-   [  3-2. (Line chart/Line plot)]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.arange(10)
plt.plot(data)

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')