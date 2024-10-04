
"""
设美女和男人各自随机出一枚硬币的正反面，收益如下表
如果美女正面 男人正面   +3
   美女反面 男人反面   +1
   一正一反  -2

问：有策略让男人一直输吗？

假设：
美女出正面的概率x  反面的概率1-x
男人出正面的概率y  反面的概率1-y
"""

#男人赢钱的数学期望

#E=3*x*y+(1-x)*(1-y)-2((x*(1-y))+((1-x)*y))
#E=8*x*y-3*x-3*y+1
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return 8 * x * y - 3 * x - 3 * y + 1
"""
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(X.ravel(), Y.ravel(), s=100 * Z.ravel())
plt.show()
"""

xnew=[round(i, 2) for i in [i/100 for i in range(101)]]
ynew=[round(i, 2) for i in [i/100 for i in range(101)]]



