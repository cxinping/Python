import tushare as ts
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import matplotlib.dates as mdates

data = ts.get_hist_data('600848', ktype='60')
data = data.head(5)

#print(data.index)
xs = [mdates.strpdate2num('%Y-%m-%d %H:%M:%S')(d ) for d in data.index ]

ax = plt.gca()  
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
    
plt.plot_date(xs, data['open'],'-')
plt.gcf().autofmt_xdate()
plt.show()



