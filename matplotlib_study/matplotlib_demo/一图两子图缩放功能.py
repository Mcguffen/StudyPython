import numpy as np
import matplotlib as mpl
mpl.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
import matplotlib.pyplot as plt
import numpy as np
from log import log
# 1.创建两个子图
# 2.分别对子图设置x y, 数据
# 3.编写点击事件 获得上一图的xy
# 4.重绘子图


def load_date():
    # 本次使用的numpy自动生成
    # 从 −π−π 到 +π+π 等间隔的 256 个值

    # 后期使用numpy加载 excel数据
    X = np.linspace(-np.pi, np.pi, 200, endpoint=True)
    C, S = np.cos(X), np.sin(X)
    # log('x = ({})'.format(X))
    # log("C=({}) \n      S=({})".format(C, S))
    return X, C, S


def onpress(event):
    # 事件处理函数
    # 当鼠标点击 src图时 zoom图 显示 放大过的src图 曲线
    axzoom = plt.subplot(212)  # 第二行的图

    if event.button != 1:
        return
    x, y = event.xdata, event.ydata
    axzoom.set_xlim(x - 0.1, x + 0.1)
    axzoom.set_ylim(y - 0.1, y + 0.1)

    event.canvas.draw()
    return


def zoom_pic():
    # 主程序 缩放图像
    # figure = plt.figure()

    # 创建主图层
    figure = plt.figure(figsize=(10, 6), dpi=100)

    # 加载曲线数据
    x, c, s = load_date()

    # 创建两个子图
    src = plt.subplot(211)  # 第一行的图 211 --> 类似(n,m,o) (n) 代表 主图分n两行 每行分成m列代表每行分成
    zoom = plt.subplot(212)  # 第二行的图

    # 根据曲线数据 根据数据设置图像的 x,y轴
    # src.set(xlim=(0, 1), ylim=(0, 1), autoscale_on=False,
    #           title='Click to zoom')
    # zoom.set(xlim=(0.1, 0.55), ylim=(0.3, 0.6), autoscale_on=False,
    #            title='Zoom window')

    # 选择颜色, 绘制曲线
    # 分别将曲线数据 加载到src zoom 图上
    src.plot(x, c, color="red", linewidth=1.0, linestyle="-", label='线')
    zoom.plot(x, c, color="red", linewidth=1.0, linestyle="-", label='线')

    # 设置横轴的上下限
    # src.axes.set_xlim(-4.0, 4.0)
    # # 设置横轴坐标点
    # src.axes.set_ybound(-1, 1)

    # 子图加载曲线数据
    # src.scatter(x, y, s, c)
    # zoom.scatter(x, y, s, c)

    # 子图加图例
    src.axes.legend(loc="best")
    zoom.axes.legend(loc="best")

    led = src.axes.get_legend()

    log('led({})'.format(led))

    figure.add_axes(src, zoom)

    figure.canvas.mpl_connect('button_press_event', onpress)

    plt.show()
    pass


def test():
    zoom_pic()
    pass


if __name__ == '__main__':
    test()
