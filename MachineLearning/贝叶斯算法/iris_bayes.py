# -*- coding: utf-8 -*-

from sklearn import datasets
from sklearn.naive_bayes import GaussianNB

iris = datasets.load_iris()

# 四个特征的名字
print( iris.feature_names )

# iris的数据集，150 个样本
data =  iris.data
print(  iris.data )
print('iris.data len=', len( iris.data) )

# 3种类型的花 ['setosa' 'versicolor' 'virginica']
print( iris.target_names )
# 转化为向量目标， setosa --> 0 , versicolor --> 1 , virginica --> 2
target = iris.target 
print( target )

###贝叶斯算法
clf = GaussianNB()
clf.fit( iris.data, iris.target)

predict =clf.predict( [iris.data[0]] )
print( 'predict=',predict )
print(' iris.data[0]=' ,  iris.data[0] )
print( "* 预测概率(属于分类标签的概率) =>", clf.predict_proba( [ iris.data[0] ] ) )

predict =clf.predict( [iris.data[149]] )
print( 'predict=',predict )
print(' iris.data[149]=' ,  iris.data[149] )

import numpy as np
data = np.array([6.2	,3.4	,5.4	,2.3])
predict =clf.predict( [data] )
print( 'predict=',predict )
print(' data=' ,  data )

# 把科学计算法数据转换为浮点型数据
def as_num(x):
    y='{:.30f}'.format(x) # 10f表示保留10位小数点的float型
    return(y)
	
