import tushare as ts
import matplotlib.pyplot as plt
from datetime import datetime

data = ts.get_hist_data('600848')
# 对时间序列进行排序
data = data.sort_index()
#print(data.index)

#前5条记录
#data = data.head(50)

xs = [datetime.strptime(d, '%Y-%m-%d').toordinal() for d in data.index ]
#print(xs)

plt.plot_date( xs , data['open'] , 'b-')
plt.gcf().autofmt_xdate()  # 自动旋转日期标记
plt.show()
