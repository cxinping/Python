import tushare as ts
import matplotlib.pyplot as plt

data = ts.get_hist_data('600848')
# 对时间进行降序排列
data = data.sort_index()
print(data)


print(data.index)
#前50条记录
#data = data.head(50)

data['open'].plot()

plt.gcf().autofmt_xdate()  # 自动旋转日期标记
plt.show()
