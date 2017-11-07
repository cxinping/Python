from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans 

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

# 打印前2行测试数据集
#print(iris_X[:2, :])
#print(iris_y)

#把数据集分为训练集和测试集，其中test_size=0.3，即测试集占总数据的 30%：
X_train, X_test, y_train, y_test = train_test_split(
iris_X, iris_y, test_size=0.3)

##print(y_train)

# 手工调整中心点，然后查看预测的准确度。
clf = KMeans(n_clusters=3)
clf.fit(X_train, y_train)
#对比用模型预测的值与真实的值，可以看到大概模拟出了数据，但是有误差，是不会完全预测正确的。还可以测试单个样本数据
#y_pred = knn.predict(  [ [6.1,	2.8 , 4.7,1.2 ] ] )
y_pred = clf.predict(X_test)
print(y_pred)

# 打印真实的测试集数据
print(y_test)

#准确率
from sklearn.metrics import  accuracy_score
print( "ACC:  %f " % accuracy_score(y_test,y_pred))
