from main import load_all_lines
from utils import log_by_time as log
import json
import openpyxl
import time
import matplotlib.pyplot as plt  # 导入绘图包
import matplotlib as mpl
import numpy as np
import pylab as pl
import scipy.signal as signal
from scipy.signal import argrelextrema

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def draw_curve():
    # 从load_all_lines加载所有区县信息信息
    #  加载数据将数据绘制到matplotlib里面

    lines = load_all_lines()
    # log("draw_curve lines = ({})".format(lines))
    for line in lines:
        td, rd = line

        # log('td({}) rd({}) i'.format(td, rd))

    pass


def isnub(s):
    # 接收一个字符串
    # 判断字符串是不是数字
    # 在选择颜色时用到
    try:
        nb = float(s)  # 将字符串转换成数字成功则返回True
        return True
    except ValueError as e:
        return False  # 如果出现异常则返回False


def load_colors_with_number(num=0):
    # 传入数字选择颜色
    # 返回所有matplotlib可用的颜色
    # 暂定可以选择24种颜色
    # 返回包含颜色字符串的数组

    colors = ['red', 'blue', 'blueviolet', 'brown', 'yellow', 'burlywood', 'darkred', 'yellowgreen', 'wheat',
              'limegreen', 'whitesmoke']
    n = num
    # if num is not number
    # 如果不是数字 错误处理 暂时不写

    # 判断num范围
    # 简单的错误处理
    if num > len(colors) or n < 0:
        num = len(colors) // 2

    # log(colors[num])
    return colors[num]
    pass


def chose_color(number=0):
    # 根据参数 返回颜色
    # 例如曲线需要选择颜色
    #
    # 1. 列出所有可用的颜色
    # 2.根据参数返回可用的颜色

    # display_all_colors()
    n = number

    color = load_colors_with_number(n)

    return color


def onpress(event):
    # 事件处理函数
    # 当鼠标点击 src图时 zoom图 显示 放大过的src图 曲线
    axzoom = plt.subplot(122)  # 第二行的图

    axsrc  = plt.subplot(121)

    axsrc.axes.get_xbound()
    axsrc.axes.get_ybound()
    log('第一张子图的x', axsrc.axes.get_xlim())
    log('第一张子图的y', axsrc.axes.get_ybound())

    if event.button != 1:
        return
    x, y = event.xdata, event.ydata
    axzoom.set_xlim(x - 0.1, x + 0.6)
    axzoom.set_ylim(y - 0.01, y + 0.01)

    event.canvas.draw()
    return


def get_limets_with_all_lines():
    pass


def find_inflection_point(larr):
    # 传入曲线数组
    # 返回曲线拐点位置
    lines = load_all_lines()

    title, x, y = lines[0]

    # arr = y
    arr = larr
    ypow = 4
    y_disdance = 0.1**ypow
    # c = np.power(10, 9)

    # 0 -- len(arr-1) 的数据
    carr = arr[:-1]
    # 1 -- 98
    cparr = arr[1:]

    # 所有数据之间的距离
    distance = abs(carr - cparr)
    # cparr = arr[1:]
    # 寻找拐点 第一个点之间距离小于 0.1的 ypow(ypow=10)的点就是拐点
    #
    for i in range(len(distance)):
        dis = distance[i]
        if dis < y_disdance:
            log("i = ", i)
            return i
        pass
    log('lencparr', y_disdance)



    pass


def get_zoomed_xy_axes_limts():
    # 接收所有曲线的信息
    # 返回合适的x, y轴的上下限
    # 曲线的x y的
    lines = load_all_lines()

    # 极值点所有x y数据
    ext_xzbs = []
    ext_yzbs = []

    # 曲线所有的x y数据
    xarrs = []
    yarrs = []

    # yarr[0]所对应的 y值是y的最小值

    #  所有曲线第一个值 都是最大值
    #  多根曲线将取最小的y作为缩放图的y上限
    first = []

    # 找出曲线范围的最大最小值
    for line in lines:
        title, td, rd = line
        xarr = td
        yarr = rd
        # log('rd = {}'.format(rd))

        f = yarr[0]
        first.append(f)

        xarrs.append(xarr)
        yarrs.append(yarr)

        # 获取当前yarr拐点
        t = find_inflection_point(yarr)
        # log('y的极值({})'.format(t))

        # 搜索y 点 左右某个 值小于某个数
        # yar =

        # 将该极值点在曲线上画出来
        # 极值点的y坐标决定 y轴上限
        # 极值点的x坐标决定 x轴上限
        xzb = xarr[t]
        yzb = yarr[t]
        ext_xzbs.append(xzb)
        ext_yzbs.append(yzb)

    # log('')
    np.array([])

    # 极值点所有x y数据
    ext_xzbs = np.array(ext_xzbs)
    ext_yzbs = np.array(ext_yzbs)

    # 曲线所有的x y数据
    xarrs = np.array(xarrs)
    yarrs = np.array(yarrs)

    first = np.array(first)

    y_max = first.min()
    # 获取当前所有曲线的xarr, yarr最大最小值
    xarr_max, xarr_min = xarrs.max(), xarrs.min()
    yarr_max, yarr_min = yarrs.max(), yarrs.min()

    ext_x_min, ext_x_max = ext_xzbs.min(), ext_xzbs.max()
    ext_y_min, ext_y_max = ext_yzbs.min(), ext_yzbs.max()

    xlim_min = xarr_min - 0.1 * xarr_min
    xlim_max = ext_x_max

    y_multiples = 100
    ylim_min = yarr_min - abs(yarr_min * 20)
    # ylim_max = ext_y_min * y_multiples
    ylim_max = yarr_min

    return xlim_min, xlim_max, ylim_min, y_max

        # 和本地的最大最小做比较
        #

        # 缩放函数
        # 1.寻找极值点
        #       寻找极值点的位置
        # 2.获取极值点附近的点数据
        #       将极值点设置为图像中心点
        #       极值点左右分别取n(n=10)个点的数据
        #       获得点x, y的均值
        #       根据均值设置图像的x轴 y轴 的上下限


        # src.plot(xzb, yzb, 'o')

    pass


def zoom_pic():

    log("start zoom")
    # 绘制散点图
    # 缩放图像
    # figure = plt.figure()

    # 创建主图层
    figure = plt.figure(figsize=(9, 6), dpi=100)
    figure.suptitle('点击左子图 右边显示缩放', fontsize=14, fontweight='bold')
    # 加载曲线数据
    # x, c, s = load_date()

    # 创建两个子图
    # 左子图
    src = plt.subplot(121)  # 第一行的图 211 --> 类似(n,m,o) (n) 代表 主图分n两行 每行分成m列代表每行分成
    # 右子图
    zoom = plt.subplot(122)  # 第二行的图

    # 设置横轴的上下限
    # src.axes.set_xlim(-4.0, 4.0)
    # # 设置横轴坐标点
    # src.axes.set_ybound(-1, 1)

    # 子图加载曲线数据
    # src.scatter(x, y, s, c)
    # zoom.scatter(x, y, s, c)

    lines = load_all_lines()
    # log("draw_curve lines = ({})".format(lines))

    # 缩放数据
    # 1.斜率
    # 2.均值
    # 根据曲线数据 根据数据设置图像的 x,y轴
    # src.set(xlim=(0, 1), ylim=(0, 1), autoscale_on=False,
    #           title='Click to zoom')
    # zoom.set(xlim=(0.1, 0.55), ylim=(0.3, 0.6), autoscale_on=False,
    #            title='Zoom window')

    i = 0

    # 极值点所有x y数据
    ext_xzbs = []
    ext_yzbs = []
    # 曲线所有的x y数据
    xarrs = []
    yarrs = []

    for line in lines:
        title, td, rd = line
        xarr = td
        yarr = rd
        # log('rd = {}'.format(rd))

        # 获取当前曲线的xarr, yarr最大最小值
        xarr_max, xarr_min = xarr.max(), xarr.min()
        yarr_max, yarr_min = yarr.max(), yarr.min()



        # 自动获取不同线条颜色
        line_color = chose_color(i)

        # 1.缩放曲线
        # 2.根据算法缩放曲线

        # 选择颜色, 绘制曲线
        # 分别将曲线数据 加载到src, zoom 图上
        src.plot(xarr, yarr, color=line_color, linewidth=2.5, linestyle='-', label='Td=({})'.format(title))  # 增加了label以便增加图例
        zoom.plot(xarr, yarr, color=line_color, linewidth=2.5, linestyle='-', label='Td=({})'.format(title))  # 增加了label以便增加图例
        # plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label='sin')  # 增加了label以便增加图例
        i += 1

        # 获取当前曲线的xarr, yarr最大最小值
        xarr_max, xarr_min = xarr.max(), xarr.min()
        yarr_max, yarr_min = yarr.max(), yarr.min()

        # 缩放函数
        # 1.寻找极值点
        #       寻找极值点的位置
        # 2.获取极值点附近的点数据
        #       将极值点设置为图像中心点
        #       极值点左右分别取n(n=10)个点的数据
        #       获得点x, y的均值
        #       根据均值设置图像的x轴 y轴 的上下限

        # 获取当前yarr极值点
        t = find_inflection_point(yarr)
        # log('y的极值({})'.format(t))

        # 将该极值点在曲线上画出来
        # 极值点的y坐标决定 y轴上限
        # 极值点的x坐标决定 x轴上限
        xzb = xarr[t]
        yzb = yarr[t]
        zoom.plot(xzb, yzb, 'o')
        # log(' 坐标点x=({})  y=({})'.format(xzb, yzb))

        # 缩放多根曲线
        # 需要将曲线的 需要zoom_xlim zoom_ylim

        # 缩放单根曲线
        # 获取曲线极值点的当前坐标
        # 设置缩放的x轴

        # 根据当前曲线的xarr, yarr最大最小值 以及极值点缩放曲线

        # 设置缩放曲线的x, y轴的范围
        # zoom_xlim = get_zoomed_xy_axes_limts(xarr_min, xzb * 5)
        # zoom_ylim = get_zoomed_xy_axes_limts(yarr_min, yzb * 200)

        # 下面部分是是操作lenged标签位置
        # src.legend(loc='best')  # 添加个图例 设置图例自动调整
        zoom.legend(loc='best')

        src.set(title='原始图像')
        zoom.set(title='缩放图像')

        figure.canvas.mpl_connect('button_press_event', onpress)
        # break

    xlim_min, xlim_max, ylim_min, ylim_max = get_zoomed_xy_axes_limts()
    zoom_xlim = (xlim_min, xlim_max)
    zoom_ylim = (ylim_min, ylim_max)

    src.set(xlim=zoom_xlim, ylim=zoom_ylim, autoscale_on=False, title='原始缩放图像')
    zoom.set(xlim=zoom_xlim, ylim=zoom_ylim, autoscale_on=False, title='再次缩放图像')

    plt.show()
    log("end zoom")
    pass


def draw_line(ratio=(0.1, 0.1), legend_position=(0.8, 0.9)):
    # 修正过的 正弦余弦图
    # ratio 是x轴 y轴偏移系数
    # legend_position为传入的lenged标签位置
    # 根据传入数据 自动调整x轴 y轴 边距大小
    # 加载数据
    # X, C, S = load_date()

    # 1. 获取曲线的数据 title, td, rd
    #      label图例 X Y = title, td, rd
    # 2.给不同曲线赋不同的颜色

    # 3.缩放

    # 创建一个8 * 6点(point)的图，并设置分辨率为80
    figure = plt.figure(figsize=(10,6), dpi=100)

    # 创建一个新的 1 * 1的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
    # figure.add_subplot(1, 1, 1)
    src = plt.subplot(211)  # 第一行的图
    zoom = plt.subplot(212)  # 第二行的图

    figure.add_axes(src, zoom)

    lines = load_all_lines()
    # log("draw_curve lines = ({})".format(lines))

    i = 0
    for line in lines:
        title, td, rd = line
        X = td
        Y = rd
        # log('rd = {}'.format(rd))

        # 自动获取不同线条颜色
        line_color = chose_color(i)
        # log('选中的颜色 = ', line_color)

        i += 1

        # 1.缩放曲线
        # 2.根据算法缩放曲线

        # 绘制曲线，使用不同颜色、连续的、宽度为 1 （像素）的线条
        # plt.plot(td, rd, color='brown',  linewidth=1.0, linestyle="-")

        # 以下 1, 2, 3 是自动调整图像的函数
        # 其实1, 2, 3 应该抽出一个设置边界的函数 暂时没看到matplotlib怎么操作画布对象 先写到这里

        # 数据用numpy加载之后
        # 1 这里获得 x 最大值最小值 y最大值最小值
        xmin, xmax = X.min(), X.max()
        ymin, ymax = Y.min(), Y.max()

        # 2 设置x,y 边界偏移程度
        # 亦可以将获得ratio 数据设置成一个函数get_border_ratio()
        rx, ry = ratio
        dx = (xmax - xmin) * rx
        dy = (ymax - ymin) * ry
        #
        # # 3 根据偏移程度 设置x轴 y轴的左右值
        # src.axes.set_xlim(xmin - dx, xmax + dx)
        # src.axes.set_ylim(ymin - dy, ymax + dy)



        # 加载曲线
        src.plot(X, Y, color=line_color, linewidth=2.5, linestyle='-', label='Td=({})'.format(title))  # 增加了label以便增加图例
        zoom.plot(X, Y, color=line_color, linewidth=2.5, linestyle='-', label='Td=({})'.format(title))  # 增加了label以便增加图例
        # plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label='sin')  # 增加了label以便增加图例

        # zoom.axes.set_xlim(0,100)
        # 下面部分是是操作lenged标签位置
        src.legend(loc='best')  # 添加个图例 设置图例自动调整
        zoom.legend(loc='best')

        figure.canvas.mpl_connect('button_press_event', onpress)

        # break
    # loc的值操纵图例的位置 取值在0 - 1之间  也可以取值为  'best'-->自动获取最好的结果  'upper left' -->左上   'upper right' -->右上等

    # draw_raw_sin_cos()

    # 在屏幕上显示

    plt.show()


def test_find_inflection_point():
    # 测试寻找拐点
    find_inflection_point([])
    pass


def test_zoom_pic():
    zoom_pic()
    pass


def test():
    # draw_curve()
    # load_colors_with_number(4)
    # draw_line()
    test_zoom_pic()
    test_find_inflection_point()
    pass


if __name__ == '__main__':
    test()
