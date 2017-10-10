# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np




x = np.linspace( -3 , 3, 50  )
y1 = 2 * x + 1
y2 = x**2 + 1

plt.figure(num=1,figsize=(10,6))
plt.plot (x,y2 )
plt.plot (x,y1,color='red', linewidth=1.0,linestyle='--')

# 设置x轴刻度的取值范围
plt.xlim((-1,2))
#设置y轴刻度的取值范围
plt.ylim((-2,3))

plt.xlabel(u"I am  x")
plt.ylabel(u"I am y ")

# 设置x轴刻度的表现方式
#new_ticks = np.linspace(-1,2,5)
#plt.xticks(new_ticks)

#plt.yticks([-2,-1.8,-1,1.22,3],
#           [ r'$really \ bad$',r'$bad$',r'$normal$',r'$good$', r'$really \ good$'] )

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# y轴设置坐标原点为1
ax.spines['bottom'].set_position(('data',1))
# x轴设置坐标原点为0
ax.spines['left'].set_position(('data',0 ))


plt.show()


