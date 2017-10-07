# -*- coding: utf-8 -*-

from sklearn.cluster import KMeans
import numpy as np
df=np.array([[3,3],[4,4],[5,5],[6,71],[6,93],[4,168],[9,779],[6,182],[7,59],[2,167]])
clf = KMeans(n_clusters=2)
s = clf.fit(df)
print(s)

#2个中心
print(clf.cluster_centers_)

#每个样本所属的簇
print(clf.labels_)

# 进行预测
print(clf.predict([[1,6]]))