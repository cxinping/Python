from numpy.random import rand#使用import导入模块numpy
import matplotlib.pyplot as plt#使用import导入模块matplotlib.pyplot
import numpy as np

x = np.linspace( -1 , 1, 50  )
y2 = x**2 + 1

fig = plt.figure(num=3,figsize=(8,5))
y1 = 2 * x + 1
plt.plot (x,y2)
plt.plot (x,y1,color='red', linewidth=1.0, linestyle='--' )


import plotly as py  # 导入plotly库并命名为py

# -------------pre def
pympl = py.offline.plot_mpl

plot_url = pympl(fig,filename=r'h:/temp/scatter_2.html', show_link=False,resize=True)

