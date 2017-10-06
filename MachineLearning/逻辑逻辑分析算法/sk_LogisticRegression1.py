
# -*- coding: utf-8 -*-

"""
逻辑回归算法

"""

import matplotlib.pyplot as plt
#显示中文
from matplotlib.font_manager import FontProperties
font=FontProperties(fname=r"c:\windows\fonts\msyh.ttc", size=10)
import numpy as np

plt.figure()
plt.axis([-6,6,0,1])
plt.grid(True)
X=np.arange(-6,6,0.1)
y=1/(1+np.e**(-X))
plt.plot(X,y,'b-')
plt.show()