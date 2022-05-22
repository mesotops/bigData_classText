# -*- coding: utf-8 -*-   [範例 3-19.極坐標系 (Polar coordinate)]    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import matplotlib.pyplot as plt
xs = [1, 2, 3, 4, 5, 6, 7]
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='polar')
plt.polar(xs, 'ro')
ax.set_title('A simple polar example')
plt.show()
