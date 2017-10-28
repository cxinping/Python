from sklearn.cluster import KMeans 
import numpy as np  
 
X = np.array([[0, 0], [1, 2], [3, 1],
              [8, 8], [9, 10], [10, 7]])

kmeans = KMeans(n_clusters=2, random_state=1).fit(X)
print('--- kmeans 标签 ---'  )
print( kmeans.labels_)

#predict = kmeans.predict([[0, 0], [4, 4]])
#print('\n--- 预测值 ---')
#print( predict )

centers = kmeans.cluster_centers_
print('\n--- kmeans 中心点 ---')
print( centers )