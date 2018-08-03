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

    log 等同于print 使用

    要格式化字符串 应该传入参数时自己自带'\n '
    from utils import log_by_time as log
    :param args:
    :param kwargs:
    :return:
    '''
    print(*args, **kwargs)


def supper_log(*args, print_time=False, fprint_time=False, file=None):

    filename = file

    # 不操作文件
    # 控制台不输出时间
    if print_time is False and file is None:
        print(*args)

    # 不操作文件
    # 输出时间
    elif print_time is True and file is None:
        dt = time_stamp()
        print(dt, *args)

    # 操作文件
    # 不输出时间
    elif print_time is None:
        log()

    # 操作文件
    # 输出时间
    else:
        with open(filename, 'a', encoding='utf-8') as f:
            print(dt, *args, file=f)


    pass


log('jdajdj', True, "tes.txt")

print('vvvvv')
print('aa', end=' ')
print('aa')
print('aa', end='ddddd')
print('aaaaa')
