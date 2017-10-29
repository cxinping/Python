# -*- coding: utf-8 -*-

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

##print(iris_X[:2, :])
##print(iris_y)

#把数据集分为训练集和测试集，其中 test_size=0.3，即测试集占总数据的 30%：
X_train, X_test, y_train, y_test = train_test_split(
    iris_X, iris_y, test_size=0.3)

##print(y_train)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
#对比用模型预测的值与真实的值，可以看到大概模拟出了数据，但是有误差，是不会完完全全预测正确的
print(knn.predict(X_test))
print(y_test)
