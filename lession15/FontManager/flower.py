# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn import datasets
import matplotlib.font_manager  # matplotlib 选择系统中文字体， 不然会乱码

myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simkai.ttf.ttf')


def load_date():
    iris = datasets.load_iris()
    x = iris.data[:, 0]  # X轴
    y = iris.data[:, 1]  # Y轴
    species = iris.target  # 种类
    x_min = x - 5
    x_max = x + 5
    y_max = x + 5
    y_min = x - 5
    return x, y, x_min, x_max, y_max,  y_min, species


def draw_date():
    x, y, x_min, x_max, y_min, y_max, species = load_date()
    plt.figure()
    plt.title('Iris 数据集 - 鸢尾花尺寸分类', fontproperties=myfont)
    plt.scatter(x, y, c=species)
    plt.xlabel('花萼长度', fontproperties=myfont)
    plt.ylabel('花萼宽度', fontproperties=myfont)
    # plt.xlim(x_min, x_max)
    # plt.ylim(y_min, y_max)
    plt.xticks
    plt.yticks


if __name__ == '__main__':
    draw_date()