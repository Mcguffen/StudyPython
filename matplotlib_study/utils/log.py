import locale
import time
'''
为什么要自己写file函数

先上总结
******结论**********
print 的file 想要的是一个对象 ( 使用write方法打开的对象)
我们传入的是文件名是一个字符串 
所以要自己写file函数

******ps********
写了log_file_is_str() 来说明 错误
test 函数中 运行 test_log_file_is_str()  查看结果
test_log_file_is_str函数已经注释


********************正文*************************
python 的print api如下
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

关于文件编码部分
file说明是
The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used.
 Since printed arguments are converted to text strings, print() cannot be used with binary mode file objects. For these,
use file.write(...) instead.
翻译过来就是 file必需是使用write方法打开的对象
file必须是具有write(string)方法的对象;
如果它不是write对象，
将使用sys.stdout 根据你的电脑的平台选择编码进行标准输出。
根据平台选择编码格式 而windows的编码为类似gbk的cp936
而python标准输出

总而言之就是使用不给 指定encodeing编码格式, 
python 的file默认编码是当前windows平台编码 
我的是win10 --> cp936, xp win7 win10 编码格式 有可能导致乱码

**********************结束***********************************
'''


def time_stamp():
    # 时间戳工具
    # 返回当前时间
    # 2018/08/03 10:14:09
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)

    return dt


def get_locale_encoding():
    #   获取当前平台的编码格式
    from sys import platform

    log = print
    log('当前平台是', platform)
    log('编码格式是 ', locale.getdefaultlocale())


def log_file_is_str(*args,   file=None, print_time=False):
    # 运行本程序会出错
    # file必需是使用write方法打开的对象
    # log_file_is_str(x, file="log.txt")
    # f = file --> 传入的f的是文件名(字符串)
    # print(x, file = f) 传入file的是一个字符串 ,所以直接打印是会出错的

    timerstr = ''
    f = file

    # 打印时间
    if print_time:
        dt = time_stamp
        # 格式化时间存入timerstr
    # *args中加入timerstr

    # 打印到文件
    print(dt, *args, file=f)


def log_to_console(*args, dt=''):
    # 控制台打印log
    # 函数无返回
    # dt log 追加时间
    # 无返回
    # dt = '' 默认为空
    # print("*args = ({})".format(*args))

    # print自带 ' ' 分割不同变量
    # 如果没有dt=='' , 可以直接 print(*args)
    # 也可以  print(dt, sep='', *args)

    # 输出log
    if dt == '':
        print(*args)
        # print(dt, sep='', *args)
    else:
        print(dt, *args)


def log_to_file(*args, file=None, dt=''):
    # 将log数据写入文件中
    # 函数无返回
    # dt 为当前时间
    # 时间可以设置为函数内生成
    # 或者外部传入
    # dt默认为空

    filename = file
    t = dt

    # 传入文件名
    if filename is None:
        # print('未传入文件名')
        pass

    # 输出log到文件中
    else:
        with open(filename, 'a', encoding='utf-8') as f:
            # print('t=({})'.format(t))

            # log是否包含时间
            if t == '':
                print(*args, file=f)
            else:
                print(t, *args, file=f)
        # print('文件保存成功')

    pass


def log(*args, file=None, print_time=False, console=True):
    # file是文件名
    # print_time log追加时间  默认关闭
    # console  log输出到控制台 默认开启
    # log 函数无返回
    timerstr = ''
    f = file
    # print("*args = ({})".format(*args))

    # log追加时间
    if print_time is True:
        timerstr = time_stamp()

    # log输出到控制台
    if console is True:
        log_to_console(*args, dt=timerstr)

    # log到文件
    if f is not None:
        log_to_file(*args, file=f, dt=timerstr)


def test_log_file_is_str():
    # 这个程序 会出错
    log('运行 log_file_is_str 会出错')
    log_file_is_str("这是错误的", print_time=True, file='测试log.txt')


def test_log():
    # log("小白菜")
    # log("小白菜", print_time=True)

    # a = '测试log'
    # b = '输出时间'
    # c = '控制台打印'
    # d = 'log到文件'

    # log(a+b, print_time=True, file='测试log.txt')
    #
    # log("测试log 输出时间 控制台打印 log到文件", print_time=True)

    log("log1 到console 不输出时间  1")
    log("log2 到console 输出时间  2", print_time=True)

    # print("log3 到文件 不输出时间 控制台打印 3")
    log("log3 到文件 不输出时间 控制台打印 3", file='测试log.txt')
    log("log4 到文件 输出时间 不控制台打印 4", print_time=True, file='测试log.txt', console=False)
    pass


def test():
    # get_locale_encoding()
    # test_log_file_is_str()  # 这个程序 会出错 演示为什么要写打开文件的函数 为什么要自己写file函数
    test_log()


if __name__ == '__main__':
    test()
