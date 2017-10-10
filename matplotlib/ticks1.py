# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

import matplotlib

x = np.linspace( -3 , 3, 50  )
y1 = 2 * x + 1
y2 = x**2 + 1

plt.figure(num=1,figsize=(10,5))
plt.plot (x,y2 )
plt.plot (x,y1,color='red', linewidth=1.0,linestyle='--')

# 设置x轴刻度的取值范围
plt.xlim((-1,2))
#设置y轴刻度的取值范围
plt.ylim((-2,3))

plt.xlabel(u"I am  x")
plt.ylabel(u"I am y ")

# 设置x轴刻度的表现方式
new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)

plt.yticks([-2,-1.8,-1,1.22,3],
           [r'$really \ bad$',r'$bad$',r'$normal$',r'$good$',r'$really \ good$'] )

plt.show()


