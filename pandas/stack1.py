import pandas as pd
import pandas_datareader.data as web

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

finance = pd.read_csv('apple_stock.csv' , converters={0:datestr2num} )
plt.plot(finance.index, finance['Open'])
plt.gcf().autofmt_xdate()  # 自动旋转日期标记
plt.show()