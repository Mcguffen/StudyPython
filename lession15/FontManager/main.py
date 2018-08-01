import time
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager  # matplotlib 选择系统中文字体， 不然会乱码
from my_front_manger import my_all_fronts


def load_data():
    # 加载x, y ,z 数据
    x = np.linspace(0, 10, 1000)
    y = np.sin(x)
    z = np.cos(x ** 2)
    return x, y, z


def craw_sin_cos(f):
    # 画出正弦余弦
    # f为指定的字体
    x, y, z = load_data()
    # myf = f
    myfont = matplotlib.font_manager.FontProperties(fname=f)
    log('myfont', myfont)
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
    plt.plot(x, z, 'b--', label="$cos(x^2)$")
    plt.xlabel("Time(s)")
    plt.ylabel("Voltage(V)")
    plt.title("正弦函数", fontproperties=myfont)
    plt.legend()
    plt.show()


