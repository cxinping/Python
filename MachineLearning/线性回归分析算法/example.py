import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

def get_data(file_name):
    # 读取房屋面积与价格历史数据，读入dataframe
    data = pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    for single_square_feet ,single_price_value in zip(data['square_feet'],data['price']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append(float(single_price_value))

    return X_parameter,Y_parameter

def linear_model_main(X_parameters, Y_parameters, predict_value):
    # 建立线性回归模型
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
	#到平面的 截距
    predictions['intercept'] = regr.intercept_
	#到平面的系数 
    predictions['coefficient'] = regr.coef_
	# 预测值
    predictions['predicted_value'] = predict_outcome
    return predictions

def show_linear_line(X_parameters,Y_parameters):
 # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters,Y_parameters,color='blue')
    plt.plot(X_parameters,regr.predict(X_parameters),color='red',linewidth=4)
    # plt.xticks(())
    # plt.yticks(())
    plt.xlabel("square_feet")
    plt.ylabel("price")
    plt.show()

X,Y = get_data('input_data.csv')
predictvalue = 700
result = linear_model_main(X,Y,predictvalue)
print("Intercept value " , result['intercept'] )
print(  "coefficient" , result['coefficient'])
print(  "Predicted value: ",result['predicted_value'] )

show_linear_line(X,Y)
