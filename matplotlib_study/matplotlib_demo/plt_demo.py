import numpy as np
import matplotlib as mpl
mpl.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
import matplotlib.pyplot as plt # 导入绘图包
labels = 'frog', 'hogs', 'dogs', 'logs' # 设定数据标签
sizes = 15, 20, 45, 10 # 设定数据
colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral' # 设定颜色
explode = 0, 0.2, 0, 0
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
plt.axis('equal')
plt.show()

# 从 −π−π 到 +π+π 等间隔的 256 个值
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)

C, S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)
plt.show()