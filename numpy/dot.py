# https://baike.baidu.com/item/%E7%9F%A9%E9%98%B5/18069 
# 两个矩阵相乘
import numpy as np

arr1 = np.array([ [1,0,2] ,[-1, 3, 1] ] )
arr2 = np.array([ [3,1] ,[2,1],[1, 0] ] )
arr3 = arr1.dot(arr2 )
print(arr3 )