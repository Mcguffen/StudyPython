from main import load_all_lines
from utils import log
import json
import openpyxl
import time
import matplotlib.pyplot as plt  # 导入绘图包
import matplotlib as mpl
import numpy as np

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
    try:
        nb = float(s) #将字符串转换成数字成功则返回True
        return True
    except ValueError as e:
        return False #如果出现异常则返回False


def load_colors_with_number(num=0):
    # 传入数字选择颜色
    # 返回所有matplotlib可用的颜色
    # 暂定可以选择24种颜色
    # 返回包含颜色字符串的数组
    cnames = {
        'blue': '#0000FF',
        'blueviolet': '#8A2BE2',
        'brown': '#A52A2A',
        'burlywood': '#DEB887',
        'darkred': '#8B0000',
        'darksalmon': '#E9967A',
        'darkseagreen': '#8FBC8F',
        'darkslateblue': '#483D8B',
        'fuchsia': '#FF00FF',
        'gainsboro': '#DCDCDC',
        'ghostwhite': '#F8F8FF',
        'lightsteelblue': '#B0C4DE',
        'lightyellow': '#FFFFE0',
        'lime': '#00FF00',
        'limegreen': '#32CD32',
        'palevioletred': '#DB7093',
        'papayawhip': '#FFEFD5',
        'peachpuff': '#FFDAB9',
        'peru': '#CD853F',
        'wheat': '#F5DEB3',
        'white': '#FFFFFF',
        'whitesmoke': '#F5F5F5',
        'yellow': '#FFFF00',
        'yellowgreen': '#9ACD32'}
    colors = list(cnames.keys())

    n = num
    # if num is not number
    # 如果不是数字 错误处理 暂时不写

    # 判断num范围
    if num > len(colors) or num < 0:
        num = len(colors) // 2

    log(colors[num])
    return colors[num]
    pass


def chose_color(number=0):
    # 根据参数 返回颜色
    # 1. 列出所有可用的颜色
    # 2.根据参数返回可用的颜色

    # display_all_colors()
    n = number

    color = load_colors_with_number(n)

    return color


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
    plt.figure()

    # 创建一个新的 1 * 1的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
    plt.subplot(1, 1, 1)

    lines = load_all_lines()
    # log("draw_curve lines = ({})".format(lines))

    # 给线条提供不重复的颜色

    i = 0
    for line in lines:
        title, td, rd = line
        X = td
        Y = rd
        # log('rd = {}'.format(rd))

        # 自动获取不同线条颜色
        line_color = chose_color(i)
        log('选中的颜色 = ', line_color)

        i += 1

        # 1.缩放曲线
        # 2.根据算法缩放曲线

        # 绘制曲线，使用不同颜色、连续的、宽度为 1 （像素）的线条
        # plt.plot(td, rd, color='brown',  linewidth=1.0, linestyle="-")

        # 以下 1, 2, 3 是自动调整图像的函数
        # 其实1, 2, 3 应该抽出一个设置边界的函数 暂时没看到matplotlib怎么操作画布对象 先写到这里

        # 数据用numpy加载之后
        # 1 这里获得 x 最大值最小值 y最大值最小值
        # xmin, xmax = X.min(), X.max()
        # ymin, ymax = C.min(), C.max()
        #
        # # 2 设置x,y 边界偏移程度
        # # 亦可以将获得ratio 数据设置成一个函数get_border_ratio()
        # rx, ry = ratio
        # dx = (xmax - xmin) * rx
        # dy = (ymax - ymin) * ry
        #
        # # 3 根据偏移程度 设置x轴 y轴的左右值
        # plt.xlim(xmin - dx, xmax + dx)
        # plt.ylim(ymin - dy, ymax + dy)

        # 下面部分是是操作lenged标签位置
        # lp 为传入的lenged标签
        # lp = legend_position


        plt.plot(X, Y, color=line_color, linewidth=2.5, linestyle='-', label='Td=({})'.format(title))  # 增加了label以便增加图例
        # plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label='sin')  # 增加了label以便增加图例
        plt.legend(loc='best')  # 添加个图例 设置图例位置
        # break
    # loc的值操纵图例的位置 取值在0 - 1之间  也可以取值为  'best'-->自动获取最好的结果  'upper left' -->左上   'upper right' -->右上等

    # draw_raw_sin_cos()

    # 在屏幕上显示
    plt.show()


def test():
    # draw_curve()
    # load_colors_with_number(4)
    draw_line()
    pass


if __name__ == '__main__':
    test()
