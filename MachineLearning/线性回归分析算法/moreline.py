# -*- coding: utf-8 -*-

import pandas as pd  
data = pd.read_csv('Advertising.csv')  

# display the last 5 rows  
#print( data.tail()   )
#print( data.shape )

import seaborn as sns  
import matplotlib.pyplot as plt   

#sns.pairplot(data, x_vars=['TV','radio','newspaper'], y_vars='Sales', size=7, aspect=0.8)  
sns.pairplot(data, x_vars=['TV','radio','newspaper'], y_vars='Sales', size=7, aspect=0.8, kind='reg')  
plt.show() 


#create a python list of feature names  
feature_cols = ['TV', 'radio', 'newspaper']  
## use the list to select a subset of the original DataFrame  
X = data[feature_cols]  
## equivalent command to do this in one line  
X = data[['TV', 'radio', 'newspaper']]  
## print the first 5 rows  
#print( X.head()  )
### check the type and shape of X  
#print( type(X)   )
#print( X.shape   )


## select a Series from the DataFrame  
y = data['Sales']  
## print the first 5 values  
#print( y.head()  )


## 构建训练集与测试集
from sklearn.cross_validation import train_test_split 
X_train,X_test, y_train, y_test = train_test_split(X, y,  test_size=0.3 ) 
#print('\n---  构建训练集与测试集 ---')
#print( X_train.shape  )
#print( y_train.shape  )
#print( X_test.shape   )
#print( y_test.shape  )
#
## sklearn的线性回归 
from sklearn.linear_model import LinearRegression  
linreg = LinearRegression()  
model=linreg.fit(X_train, y_train)  
#print('\n---  sklearn的线性回归   ---')
#print( '截距 intercept_=' , linreg.intercept_   )
#print( '斜率linreg.coef_ =' ,linreg.coef_  )
 
## pair the feature names with the coefficients  
feature = zip(feature_cols, linreg.coef_)  
print( list(feature) )


# 预测数据
y_pred = linreg.predict(X_test) 
#print('\n---  预测数据   ---') 
#print( 'y_pred=', y_pred   )
#
#
## 均方根误差(Root Mean Squared Error, RMSE)
#print( type(y_pred),type(y_test)   )
#print( len(y_pred),len(y_test)   )
#print( y_pred.shape,y_test.shape   )

import numpy as np  
sum_mean=0  
for i in range(len(y_pred)):  
    sum_mean+=(y_pred[i]-y_test.values[i])**2  
    sum_erro=np.sqrt(sum_mean/50)  
 
print( "损失函数:",sum_erro   )



## 做ROC曲线 
import matplotlib.pyplot as plt  
plt.figure()  
plt.plot(range(len(y_pred)),y_pred,'b',label="predict")  
plt.plot(range(len(y_pred)),y_test,'r',label="test")  
plt.legend(loc="upper right") #显示图中的标签  
plt.xlabel("the number of sales")  
plt.ylabel('value of sales')  
plt.show()  




