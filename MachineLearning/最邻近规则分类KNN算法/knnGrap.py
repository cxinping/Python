import numpy as np
import matplotlib.pyplot as plt

# 定义四个点的坐标
a1 = np.array([1, 1])
a2 = np.array([1, 2])
b1 = np.array([3, 3])
b2 = np.array([3, 4])

# 四个点坐标分别赋值给X,Y
X1, Y1 = a1
X2, Y2 = a2
X3, Y3 = b1
X4, Y4 = b2

plt.title('show data')
plt.scatter(X1, Y1, color="blue", label="a1")
plt.scatter(X2, Y2, color="blue", label="a2")
plt.scatter(X3, Y3, color="red", label="b1")
plt.scatter(X4, Y4, color="red", label="b2")
plt.legend(loc='upper left')

plt.annotate(r'a1(1,1)', xy=(X1, Y1), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'a2(1,2)', xy=(X2, Y2), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'b1(3,3)', xy=(X3, Y3), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'b2(3,4)', xy=(X4, Y4), xycoords='data', xytext=(+10, +30), textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.show()
