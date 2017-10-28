# -*- coding: utf-8 -*-

import tushare as ts
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

import numpy as np
import pandas as pd


df = ts.get_hist_data('600848')

def makeChange(v):
    if( v > 0):
        return 1
    elif( v < 0):
        return -1
    else:
        return 0

changeVl = df.iloc[:, 5]
changeVl =changeVl.apply(makeChange)
df['changeVl'] = changeVl

file ='todaystock.csv'
#df.to_csv(file, encoding='utf-8', index=False)

df = pd.read_csv( file )
feature_cols = ['open', 'high', 'close']  
X = df[feature_cols]  
y = df['changeVl']  
#df['changeLabel'] = changeVl
#
#features = df.iloc[0:5,0:4]
#label = df['changeLabel']
##
X_train,X_test, y_train, y_test =  train_test_split( X, y, 
                                test_size = 0.2, random_state = 0)
clf = GaussianNB().fit(X_test, y_test) 

predict_data =  X.iloc[3]#
print('predict_data=\n' , predict_data)

i = [ predict_data]
predict = clf.predict(i)
print('predict=' , predict)




