import matplotlib.pyplot as plt
import numpy as np

# 解决显示中文乱码问题
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def runPlt():
    plt.figure()
    plt.title('披萨价格和直径数据')
    plt.xlabel('直径(英寸)')
    plt.ylabel('价格(美元)')
    plt.axis([0,25,0,25])
    plt.grid(True)
        
    return plt

plt = runPlt()
X = [ [6], [8], [10] , [14] , [18] ]
y = [ 7, 9, 13, 17.5 , 18]
plt.plot(X,y, linestyle='', marker='.')

from sklearn.linear_model import LinearRegression
#创建并拟合模型
model = LinearRegression()
model.fit( X ,y)
print('预测一张12英寸披萨的价格：' , model.predict( 12 ) )

intercept = model.intercept_
coef = model.coef_[0]
print('截距 intercept=' , intercept)
print('斜率 coef=' , coef )
print('一元线性公式 ','y =  {0} * x + {1} '.format(coef, intercept ))

yPr= model.predict(X)
plt.plot(X,yPr  ) 
#画出每个数据集的残差值
for idx, x in enumerate(X ):
  
    plt.plot( [x,x] , [y[idx] , yPr[idx]] , 'g-')
    


plt.show()
