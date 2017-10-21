import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
#拟合数据
clf.fit(X, Y)

print( "* 预测分类结果(属于哪个分类标签) =>" , clf.predict([[-0.8, -1]]))
print( "* 预测概率(属于分类标签的概率) =>", clf.predict_proba([[-0.8, -1]]))

# 把科学计算法数据转换为浮点型数据
def as_num(x):
    y='{:.10f}'.format(x) # 10f表示保留10位小数点的float型
    return(y)


#print( as_num(  -5.05653266e-08 ) )
#print( as_num( -1.67999998e+01 ) )