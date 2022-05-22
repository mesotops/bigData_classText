# -*- coding: utf-8 -*-   [  3-1.折線圖(Line chart /Line plot)]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
import matplotlib.pyplot as plt
dot1=[3,4,2,1]
dot2=[5,1,2,4]
plt.plot(dot1)
plt.plot(dot2)
plt.ylabel('The name of the Y axis') 
plt.xlabel(' The name of the X axis')        
plt.title("The name of the image's Theme")    
plt.show()
plt.savefig('Line chart.jpg')