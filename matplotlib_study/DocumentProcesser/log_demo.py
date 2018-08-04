import time


def time_stamp():
    # 时间戳工具
    # 返回当前时间
    # 2018/08/03 10:14:09
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)

    return dt


def log(*args, **kwargs):
    '''
    断点调试工具,可以接收任意多参数
    要格式化字符串 应该传入参数时自己自带'\n '
    from utils import log_by_time as log
    :param args:
    :param kwargs:
    :return:
    '''
    print(*args, **kwargs)


def log_by_time(*args, **kwargs):
    '''
    控制台输出带时间的log
    from utils import log_by_time as log_t
    :param args:
    :param kwargs:
    :return:
    '''
    dt = time_stamp()
    print(dt, *args, **kwargs)


def log_to_file(*args, **kwargs):
    '''
    # 接收任意参数
    # 将log文件写入到log.file.txt文件中
    # 引入log可以这样写
    from utils import log_to_file as log_f
    '''
    filename = 'log.file.txt'
    dt = time_stamp()

    # 本地不存在该log文件创建 存在则追加log到文件中
    with open(filename, 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


def log_with_file_and_console(*args, **kwargs):

    '''
    # 控制台打印log
    # 将log文件写入到log.file.txt文件中
    # 其他文件引入本log函数可以这样写
    from utils import log_with_file_and_console as log_w
    :param args:
    :param kwargs:
    :return:
    '''

    filename = 'log.file.txt'
    dt = time_stamp()
    print(dt, *args, **kwargs)

    # 本地不存在该文件创建 存在则追加log到文件中
    with open(filename, 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


def test():
    t1 = 0
    t2 = 1
    # t3是空字符串 '防止变量为空, 输出时需要加括号, ({})'.format(t3)
    t3 = ''
    log("这是不带时间的log \n 自行美化化字符串".format(t1))
    log_by_time('这是带时间的log, 防止变量值为空, 输出时需要加括号,t3=({})'.format(t3))
    log_to_file('控制台不显示log输出 当前时间 log 到文件中, ', t1, t2)
    log_with_file_and_console('输出 当前时间 log 到文件中, 控制台显示t1={} t2={}'.format(t1, t2))
    pass


if __name__ == '__main__':
    test()

