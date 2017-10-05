
#1 构件树
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

#2 训练完成后，导出 iris 数据集训练树的例子
from sklearn.externals.six import StringIO
with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

#3 dot -Tpdf iris.dot -o iris.pdf

clf.predict(iris.data[:1, :])
