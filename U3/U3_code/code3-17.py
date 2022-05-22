# -*- coding: utf-8 -*-   [範例 3-17.箱型圖 (Box plot)]    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import pandas as pd
import matplotlib.pyplot as plt

data = [1, 2, 3, 4, 5, 6, 7, 8]

df = pd.DataFrame(data)
print(df.describe())
df.plot.box(title="Box Chart")
plt.grid(linestyle="--", alpha=0.3)
plt.show()