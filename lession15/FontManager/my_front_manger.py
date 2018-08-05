# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 11:40:51 2018

@author: Administrator
"""
'F:\CODE\FontManager\simfang.ttf'
import time
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager  # matplotlib 选择系统中文字体， 不然会乱码
# f = 'C:/Windows/Fonts/simhei.ttf'
#
# myfont = matplotlib.font_manager.FontProperties(fname=f)


def log(*args, **kwargs):
    # 自己写的调试的工具函数
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)


def find_files_with_suf(file_dir, name='.ttf'):
    # 寻找指定文件夹下 指定结尾的文件
    rs = []
    # print('inner find file with ')
    for root, dirs, files in os.walk(file_dir):
        # log('files({})'.format(files))
        for file in files:
            if os.path.splitext(file)[1] == name:
                rs.append(os.path.join(root, file))

    return rs
#
#
# def find_all_front(file_dir='front'):
#     # 查看本地有多少字体
#     # suf = '**.' + 'ttf'
#     now_dir = os.getcwd()
#     # f = 'r' + now_dir + suf
#     # # file =
#     # fronts = glob.glob(f)
#     now_dir = now_dir.replace('\\', '/')
#     log('now_dir sdsd = ({})'.format(now_dir))
#     date = {}
#     for root, dirs, fs in os.walk(file_dir):
#         # print(root) #当前目录路径
#         # print(dirs) #当前路径下所有子目录
#         # print(files) #当前路径下所有非目录子文件
#         files = fs
#     #     log('ddddd', root, files, '\n')
#     # log('root =({}) \n dirs =({})\n files = ({})'.format(root, dirs, files))
#     rs = []
#     for i in range(len(files)):
#         f = files[i]
#         # log('front', i, f)
#         p = now_dir + '/' + f
#         date[i] = f
#         rs.append(p)
#         # log('rs = ({})'.format(rs))
#
#     # f = now_dir + '/' + f
#     return files, rs


def my_all_fronts(f='front'):
    # 测试的中文字体放在当前的/front 文件夹下
    # 返回front 所有的中文字体
    # f_dir = 'C:/Windows/Fonts' 这是windows本地字体所在位置
    # log('inner my_windows_fronts')

    front_dir = f
    # 获取当前文件夹位置  修改路径格式 'C:\Windows\Fonts' -->  'C:/Windows/Fonts'
    now_dir = os.getcwd()
    now_dir = now_dir.replace('\\', '/')
    # log('now_dir  = ({})'.format(now_dir))
    f_dir = now_dir + '/' + front_dir

    # frons = find_files_with_suf(f_dir, )
    # 字体格式后缀为'.ttf', '.TTF'
    suf = ('.ttf', '.TTF')
    rs = []
    for i in range(len(suf)):
        end = suf[i]
        f = find_files_with_suf(f_dir, end)
        rs.append(f)
    # log('rs=({})'.format(rs))
    fronts = rs
    fs = [i for item in fronts for i in item]
    # log('fs = ({})'.format(fs))

    log('rs**** ({})'.format(fs))
    return fs


def show_all_front():
    fronts = my_all_fronts()
    print('**********当前字体*********')
    for i in range(len(fronts)):
        f = fronts[i]
        f = f.replace('\\','/')
        print('字体', i, f)


def chose_my_front():
    # 选择某个字体
    print('**********选择字体*********')
    fronts = my_all_fronts()
    show_all_front()
    c = input('\n**********输入数字选择字体*********:')
    c = int(c)
    if c < len(fronts):
        f = fronts[int(c)]
    else:
        print('out range')
    print('已选择({})字体'.format(f), c)
    font = fronts[c]
    font = font.replace('\\', '/')
    myfont = matplotlib.font_manager.FontProperties(fname=font)

    log('end chose front({})'.format(font))
    return myfont

#
# def chose_my_font():
#     # 选择字体
#     fronts = my_all_fronts()
#     font =  fronts[1]
#     myfont = matplotlib.font_manager.FontProperties(fname=font)
#
#     return myfont


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
    # myfont = chose_my_front()
    log('myfont', myfont)
    plt.figure(figsize=(8, 4))
    log('craw_sin_cos end chose front')
    plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
    plt.plot(x, z, 'b--', label="$cos(x^2)$")
    plt.xlabel("Time(s)")
    plt.ylabel("Voltage(V)")
    plt.title("正弦函数", fontproperties=myfont)
    plt.legend()

    plt.show()


def test_my_front():
    my_all_fronts()
    print('\n')
    my_all_fronts('source_code_pro')
    pass


def test_craw_with_front():
    fs = my_all_fronts()
    log('fs = ({})'.format(fs))
    for i in range(len(fs)):
        f = fs[i]
        log('f = ({})'.format(f), i)
        # load_data()
        # c = 'C:/Windows/Fonts\\simfang.ttf'
        # C:\Users\Administrator\PycharmProjects\StudyPythonWeb\lession15\FontManager\front
        craw_sin_cos(f)
        # break


def test_craw_with_front2():
    fs = my_all_fronts('front')

    # fs = [i for item in fronts for i in item]
    log('fs = ({})'.format(fs))
    for i in range(len(fs)):
        f = fs[i]
        log('f = ({})'.format(f), i)
        # load_data()
        # c = 'C:/Windows/Fonts\\simfang.ttf'
        # C:\Users\Administrator\PycharmProjects\StudyPythonWeb\lession15\FontManager\front
        craw_sin_cos(f)


def my_front():
    show_all_front()
    test_craw_with_front2()

    pass


def test():
    # test_my_windows_front()
    # test_craw_with_front()
    test_craw_with_front2()
    # test_my_windows_front()
    my_front()
    pass


def main():
    f = my_all_fronts()
    log('all fronts({})'.format(f))
    front = f[1]
    craw_sin_cos(front)
    pass


if __name__ == '__main__':
    test()
    # main()





