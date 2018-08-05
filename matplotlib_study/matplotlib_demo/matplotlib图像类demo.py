import numpy as np
import matplotlib as mpl
mpl.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号
import matplotlib.pyplot as plt # 导入绘图包


def test_subplot():

    a = plt.subplot(221)  # 第一行的左图
    b = plt.subplot(222)  # 第一行的右图
    c = plt.subplot(212)  # 第二整行
    # plt.show()

    return a, b, c


def test():
    fig, ax = plt.subplots()
    figure = plt.figure(figsize=(10, 6), dpi=100)
    # a = test_subplot()
    # a.title("这是a的title")
    # a = plt.subplot(211)  # 第一行的左图
    # b = plt.subplot(212)  # 第一行的左图
    # c = plt.subplot(414)  # 第一行的左图

    # figure.add_axes(a, b)
    # figure.add_axes(c)

    # figure.add_subplot(1, 1, 1)

    # figure.show()

    plt.show()
    pass


if __name__ == '__main__':
    test()
