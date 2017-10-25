# -*- coding: utf-8 -*-


#from sklearn.linear_model import LinearRegression
#import numpy as np
#
#X =[ [208],	[152],	[113],	[227],	[137],	[238],	[178],	[104],	[191],	[130] ]
#y = [ [21.6],	[15.5],	[10.4],	[31.0],[13.0], [32.4],	[19.0],	[10.4],[	19.0],	[11.8] ]
#
#model = LinearRegression()
#model.fit(X,y)
#
#print('残差平方和: %.2f' % np.mean(  (model.predict(X) - y )**2 ) )
#print( model.predict(X)  )

###最小二乘法试验###
import numpy as np
from scipy.optimize import leastsq

###采样点(Xi,Yi)###
Xi=np.array([208,	152,	113,	227,	137,	238,	178,	104,	191,	130])
Yi=np.array([21.6,	15.5,	10.4,	31.0,	13.0,	32.4,	19.0,	10.4,	19.0,	11.8])

###需要拟合的函数func及误差error###
def func(p,x):
    k,b=p
    return k*x+b

def error(p,x,y,s):
    print( s)
    return func(p,x)-y #x、y都是列表，故返回值也是个列表

#TEST
p0=[100,2]
#print( error(p0,Xi,Yi) )

###主函数从此开始###
s="Test the number of iteration" #试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的k、b
Para=leastsq(error,p0,args=(Xi,Yi,s)) #把error函数中除了p以外的参数打包到args中
k,b=Para[0]
print("k=",k,'\n',"b=",b)