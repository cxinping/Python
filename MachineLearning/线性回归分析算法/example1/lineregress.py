# -*- coding: utf-8 -*-

import numpy as np
import os
import matplotlib.pyplot as plt

def drawScatterDiagram(fileName):
    #改变工作路径到数据文件存放的地方
    os.chdir(r"E:\temp")
    xcord=[];ycord=[]
    fr=open(fileName)
    lines = fr.readlines()
    #print( lines[1] )
    
    x_val = lines[0]
    y_val = lines[1]
    
    x_arr = x_val.strip().split(',')
    for x in x_arr:
        #print('x=', x.strip())
        xcord.append(float( x.strip() ));

    y_arr = y_val.strip().split(',')
    for y in y_arr:
        #print('y=', y.strip())
        ycord.append(float( y.strip() ));  

    #print(xcord)    
    #print(ycord)    

    plt.scatter(xcord,ycord,s=30,c='red',marker='s')
    #a=0.1965;b=-14.486
    #a=0.1612;b=-8.6394
    a=0.16123 ;b= 0.1097
    x=np.arange(90.0,250.0,0.1)
    y=a*x+b
    plt.plot(x,y)
    
    plt.show()
    
fileName = 'input_data.txt'    
drawScatterDiagram(fileName)
