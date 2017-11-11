import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def datestr2num(s):
    return mdates.strpdate2num('%Y-%m-%d')(s)

#finance = pd.read_csv('amzn_stock.csv' , converters={0:datestr2num} )
finance = pd.read_csv('alibaba_stock.csv' , converters={0:datestr2num} )
#finance = finance.head(10)
plt.plot_date(finance['Date'],finance['Open'],'b-')
plt.gcf().autofmt_xdate()  # 自动旋转日期标记
plt.show()
