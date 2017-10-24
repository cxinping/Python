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

#拟合之后，模型可以用来样本分类：
predict = clf.predict(iris.data[:1, :])
print( 'predict=',predict )

#每个分类的概率能被预测，即某个叶子中，该分类样本的占比。
predict_proba = clf.predict_proba(iris.data[:1, :])
print( 'predict_proba=',predict_proba )
