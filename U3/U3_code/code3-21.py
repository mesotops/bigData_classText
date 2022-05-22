# -*- coding: utf-8 -*-   [範例 3-21.主題河流圖 (Theme River）]   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100)
y1 = np.random.randint(20,35,100)
y2 = np.tan(x/10)
y3 = np.sin(x)*10

y = np.vstack([y1, y2, y3])

labels = ["F1 ", "F2", "F3"]

plt.figure()
plt.stackplot(x, y1, y2, y3, labels=labels, baseline='sym')
plt.legend(loc='upper left')
plt.xlabel('Number Progression')
plt.ylabel('Stack')
plt.title('Theme River Stack Plot Example')
plt.ylim(-50,50)
plt.show()