from loadlines import load_all_lines
from utils import log as log
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

# 只需要对x轴放大
#


def load_colors_with_number(num=0):
    # 传入数字选择颜色
    # 返回所有matplotlib可用的颜色
    # 暂定可以选择12种颜色
    # 返回包含颜色字符串
    from config import colors as line_colors

    n = num
    # if num is not number
    # 如果不是数字 错误处理 暂时不写

    # 判断num范围
    # 简单的错误处理
    if num > len(line_colors) or n < 0:
        num = len(line_colors) // 2

    # log(colors[num])
    return line_colors[num]
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
    # 当鼠标点击 src图时 放大 显示在 zoom图

    axzoom = plt.subplot(122)  # 第二行的图
    axsrc = plt.subplot(121)

    axsrc.axes.get_xbound()
    axsrc.axes.get_ybound()

    xlim = axsrc.axes.get_xbound()
    ylim = axsrc.axes.get_ybound()

    # src放大magni_time倍
    magni_time = 20
    xlim = np.array(xlim) / magni_time
    ylim = np.array(ylim) / magni_time

    log('放大倍数 = ({})'.format(magni_time))
    log('第一张子图的x范围', axsrc.axes.get_xlim())
    log('第一张子图的y范围', axsrc.axes.get_ybound())
    # log('xlim', xlim)

    if event.button != 1:
        return
    x, y = event.xdata, event.ydata
    x = np.array(x)

    # 设置放大之后的边界
    axzoom.set_xlim(x - 0.1, x + xlim[1])
    axzoom.set_ylim(y - ylim[1] * 0.1, y + ylim[1])

    event.canvas.draw()
    return

def onpress_lend(event):
    # 事件处理函数
    # 当鼠标点击 src图时 放大 显示在 zoom图

    axzoom = plt.subplot(111)  # 第二行的图

    axzoom.axes.get_xbound()
    axzoom.axes.get_ybound()
    # log('放大倍数 = ({})'.format(magni_time))

    # log('xlim', xlim)
    if event.button != 1:
        return
    x, y = event.xdata, event.ydata
    x = np.array(x)

    # 设置放大之后的边界
    axzoom.set_xlim(x - 0.1, x + xlim[1])
    axzoom.set_ylim(y - ylim[1] * 0.1, y + ylim[1])

    event.canvas.draw()
    return


def find_inflection_point(larr):
    # 传入曲线数组 larr
    # 返回曲线拐点 位置

    arr = larr

    # ypow决定左右点距离是0.1的几次方
    ypow = 4
    y_disdance = 0.1 ** ypow

    # 寻找拐点 第一个点之间距离小于 0.1的 ypow次方(ypow=4)的点就是拐点
    #
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) < y_disdance:
            # log("当前拐点的位置i = ", i)
            return i
    # log('所选择的值', y_disdance)


def get_zoomed_x_axes_limts():
    # 接收所有曲线的信息
    # 根据缩放函数
    # 返回合适的x轴的上下限
    # 缩放函数
    # 1.寻找拐点
    #       寻找拐点的位置
    # 2.获取极值点附近的点数据
    #       获取所以拐点的数据
    #       拐点的y坐标决定 y轴上限
    #       拐点的x坐标决定 x轴上限
    #       获得点x, y的均值
    #       根据均值设置图像的x轴 y轴 的上下限

    lines = load_all_lines()

    # 所有曲线拐点所有x y数据
    ext_xzbs = []
    ext_yzbs = []

    #  所有曲线第一个值 都是最大值
    #  多根曲线将取最小的y作为缩放图的y上限

    # 获取任意一根曲线的第一个点上的x作为最小值x
    first = []

    # 找出曲线范围的最大最小值
    for line in lines:
        title, td, rd = line
        xarr = td
        yarr = rd

        f = xarr[0]
        first.append(f)
        # 获取当前拐点位置
        t = find_inflection_point(yarr)
        # 搜索y 点 左右某个 值小于某个数
        # 极值点的y坐标决定 y轴上限
        # 极值点的x坐标决定 x轴上限
        xzb = xarr[t]
        yzb = yarr[t]
        ext_xzbs.append(xzb)
        ext_yzbs.append(yzb)

    # 获取任意一根曲线的第一个点上的最小的x
    # 作为最小值x
    first = np.array(first)
    xarr_min = first.min()

    # 所有拐点的x y数据
    ext_xzbs = np.array(ext_xzbs)
    ext_yzbs = np.array(ext_yzbs)

    # 所有曲线拐点x的最大值
    ext_x_min, ext_x_max = ext_xzbs.min(), ext_xzbs.max()
    # ext_y_min, ext_y_max = ext_yzbs.min(), ext_yzbs.max()

    # 调整曲线的边界
    # ylim_min 根据xlim_max的最大的千分之一调整
    dis = 0.03
    ydis = 0.001

    xlim_min = xarr_min - dis * ext_x_max
    xlim_max = ext_x_max

    # ylim_min = yarr_min - abs(xlim_max * ydis)
    # ylim_max = ext_y_min * y_multiples
    # ylim_max = first.max()

    return xlim_min, xlim_max
    pass


def zoom_pic():
    # 绘制散点图
    # 缩放图像
    # figure = plt.figure()

    # 创建主图层
    figure = plt.figure(figsize=(9, 6), dpi=100)
    # figure.suptitle('点击左子图 右边显示放大10倍的细节', fontsize=14, fontweight='bold')
    # 加载曲线数据
    # x, c, s = load_date()

    # 创建两个子图
    # 左子图
    src = plt.subplot(111)  # 第一行的图 211 --> 类似(n,m,o) (n) 代表 主图分n两行 每行分成m列代表每行分成

    # 记载所有曲线信息
    lines = load_all_lines()
    # log("lines = ({})".format(lines))

    # i是曲线的颜色参数
    i = 0
    for line in lines:
        title, rd, Td = line
        xarr = rd
        yarr = Td

        # log('rd = {}'.format(rd))
        # 自动获取不同线条颜色
        line_color = chose_color(i)
        i += 1

        # 选择颜色, 绘制曲线
        # 分别将曲线数据 加载到src图上
        src.plot(xarr, yarr, color=line_color, linewidth=2.5, linestyle='-',
                 label='Td=({})'.format(title))  # 增加了label以便增加图例

        # 获取当前yarr拐点位置
        t = find_inflection_point(yarr)
        # log('y的拐点({})'.format(t))
        # 将拐点显示出来
        xzb = xarr[t]
        yzb = yarr[t]
        src.plot(xzb, yzb, 'o')

        # 下面部分是是操作lenged标签位置
        src.legend(loc='best')  # 添加个图例 设置图例自动调整

    # 根据所有拐点的数据
    # 设置src缩放图的x轴上下限 和title
    xlim_min, xlim_max = get_zoomed_x_axes_limts()
    zoom_xlim = (xlim_min, xlim_max)
    # zoom_ylim = (ylim_min, ylim_max)
    src.set(xlim=zoom_xlim, autoscale_on=False, title='缩放图像')

    # 设置图例可拖动
    leg = plt.legend()
    if leg:
        leg.draggable()

    # 显示图像
    plt.show()
    pass


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
    test_zoom_pic()
    test_find_inflection_point()
    pass


if __name__ == '__main__':
    test()
