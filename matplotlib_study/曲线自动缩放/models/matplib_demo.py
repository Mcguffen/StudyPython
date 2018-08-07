import matplotlib.pyplot as plt  # 导入绘图包
import matplotlib as mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 一个例子
# 我们将从简到繁：先尝试用默认配置在同一张图上绘制正弦和余弦函数图像，然后逐步美化它。
# 让我们先生成正弦和余弦函数的一些值：
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)


def log(*args, **kwargs):
    '''
    断点调试工具,可以接收任意多参数

    log 等同于print 使用

    要格式化字符串 应该传入参数时自己自带'\n '
    from utils import log_by_time as log
    :param args:
    :param kwargs:
    :return:
    '''
    print("log : ", *args, **kwargs)


def load_date():
    # 本次使用的numpy自动生成
    # 从 −π−π 到 +π+π 等间隔的 256 个值

    # 后期使用numpy加载 excel数据
    X = np.linspace(-np.pi, np.pi, 200, endpoint=True)
    C, S = np.cos(X), np.sin(X)
    # log('x = ({})'.format(X))
    # log("C=({}) \n      S=({})".format(C, S))
    return X, C, S


def draw_raw_sin_cos():
    # 使用默认的参数画正弦余弦图

    # 加载数据
    X, C, S = load_date()

    # 创建一个8 * 6点(point)的图，并设置分辨率为80
    plt.figure(figsize=(8, 6), dpi=80)

    # 创建一个新的 1 * 1的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
    plt.subplot(1, 1, 1)

    # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
    plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")
    # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
    plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

    # 设置横轴的上下限
    plt.xlim(-4.0, 4.0)
    # 设置横轴坐标点
    plt.xticks(np.linspace(-4, 4, 9, endpoint=True))

    # 设置纵轴的上下限
    plt.ylim(-1.0, 1.0)
    # 设置纵轴坐标点
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

    # 在屏幕上显示
    plt.show()


def draw_after_revise(ratio=(0.1, 0.1), legend_position=(0.8, 0.9)):
    # 修正过的 正弦余弦图
    # ratio 是x轴 y轴偏移系数
    # legend_position为传入的lenged标签位置
    # 根据传入数据 自动调整x轴 y轴 边距大小
    # 加载数据
    X, C, S = load_date()

    # 创建一个8 * 6点(point)的图，并设置分辨率为80
    plt.figure(figsize=(8, 6), dpi=80)

    # 创建一个新的 1 * 1的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
    plt.subplot(1, 1, 1)

    # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
    plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")
    # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
    plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

    # 以下 1, 2, 3 是自动调整图像的函数
    # 其实1, 2, 3 应该抽出一个设置边界的函数 暂时没看到matplotlib怎么操作画布对象 先写到这里

    # 数据用numpy加载之后
    # 1 这里获得 x 最大值最小值 y最大值最小值
    xmin, xmax = X.min(), X.max()
    ymin, ymax = C.min(), C.max()

    # 2 设置x,y 边界偏移程度
    # 亦可以将获得ratio 数据设置成一个函数get_border_ratio()
    rx, ry = ratio
    dx = (xmax - xmin) * rx
    dy = (ymax - ymin) * ry

    # 3 根据偏移程度 设置x轴 y轴的左右值
    plt.xlim(xmin - dx, xmax + dx)
    plt.ylim(ymin - dy, ymax + dy)

    # 下面部分是是操作lenged标签位置
    # lp 为传入的lenged标签
    lp = legend_position
    plt.plot(X, C, color='blue', linewidth=2.5, linestyle='-', label='cos')  # 增加了label以便增加图例
    plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label='sin')  # 增加了label以便增加图例
    plt.legend(loc=lp)  # 添加个图例 设置图例位置
    # loc的值操纵图例的位置 取值在0 - 1之间  也可以取值为  'best'-->自动获取最好的结果  'upper left' -->左上   'upper right' -->右上等

    # draw_raw_sin_cos()

    # 在屏幕上显示
    plt.show()
    pass


def test_draw_after_revise():
    # 这是一个半自动化的测试函数
    # r开头的ratio 是 lp表示 y轴偏移系数legend_position
    # ratio 是x轴 y轴偏移系数legend_position
    # legend_position为传入的lenged标签位置

    r1 = (0, 0)
    r2 = (0.1, 0.1)
    r3 = (0.3, 0.2)

    lp0 = (0, 0)
    lp1 = (0.1, 0.1)
    lp2 = (0.5, 0.5)
    lp3 = (0.8, 0.9)
    lp4 = (1, 1)

    # 测试的值
    test_items = [
        (r1, lp1),
        (r2, lp2),
        (r2, lp2),
        (r3, lp0),
        (r3, lp1),
        (r3, lp2),
        (r3, lp3),
        (r3, lp4),

    ]

    # 依次测试函数
    # i是计数器

    i = 1
    for t in test_items:
        r, v = t
        log('测试第({})次 偏移系数({}) legend_position({})'.format(i, r, v))
        draw_after_revise(r, v)
        i += 1


def test_load_date():
    load_date()
    pass


def test():
    # draw_raw_sin_cos()
    # draw_after_revise()
    test_draw_after_revise()
    # draw_pic()
    # test_load_date()
    pass


if __name__ == '__main__':
    test()
