import time


def time_stamp():
    # 时间戳工具
    # 返回当前时间
    # 2018/08/03 10:14:09
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)

    return dt


def log_to_file(*args, file=None, dt=False):
    # 将log数据写入文件中
    # dt 控制是否追加当前时间
    filename = file

    if filename is None:
        return '未传入文件名'

    # 输出不带时间的log到文件中
    elif dt is False:
        with open(filename, 'a', encoding='utf-8') as f:
            print(*args, file=f)

    # 输出带时间的log到文件中
    else:
        dt = time_stamp()
        with open(filename, 'a', encoding='utf-8') as f:
            print(dt, *args, file=f)
    pass


def log(*args, print_to_console=False, print_time=False, file=None):
    # log 断点调试函数
    # print_to_console 打印到控制台
    # print_time 打印当前时间
    # file 写入到文件中去 例如 file ='log.txt' 写入到log.txt文件中

    filename = file

    # print('filename = ', filename)
    # 不操作文件
    # 控制台不输出时间 1
    if print_time is False and file is None:
        '不操作文件控制台不输出时间'

        print(*args)

    # 不操作文件
    # 输出时间   2
    elif print_time is True and file is None:
        dt = time_stamp()
        print(dt, *args)

    # 操作文件   3
    # 不输出时间
    elif print_time is False and file is not None:
        log_to_file(*args, file=filename)

    # 操作文件
    # 输出带时间log到文件  4
    elif print_to_console is False and print_time is True and file is not None:
        log_to_file(*args, file=filename, dt=True)

    # 操作文件
    # 输出带时间log到文件 5
    # 控制台输出log
    elif print_to_console is True and print_time is True and file is not None:
        dt = time_stamp()
        print(dt, *args)
        log_to_file(*args, file=filename, dt=True)

    # 操作文件
    # log 不带时间
    # 输出log到文件  6
    # 控制台输出log
    else:
        print(*args)
        log_to_file(*args, file=filename, dt=False)




    # 操作文件
    #
    # 控制台输出带时间的log信息 并写入文件


# log('jdajdj', True, "tes.txt")

# print('vvvvv')
# print('aa', end=' ')
# print('aa')
# print('aa', end='ddddd')
# print('aaaaa')


def test_log():
    a = 1
    b = 2

    # log('下水道卡数据库')
    # log('下水道卡数据库', 'CASD', 'CASD')
    # log('下水道卡数据库')
    # log('下水道卡数据库')
    log('测试log1')
    log('测试log2', print_time=True)
    log('测试log3', file="test_log.txt")
    log('测试log4', print_time=True, file="test_log.txt")
    # log('测试log5', print_time=True)
    log('测试log5', print_to_console=False, print_time=True, file="test_log.txt")
    log('测试log6', print_to_console=True, file="test_log.txt")

    # log('测试log1', True, file="tes.txt")



if __name__ == '__main__':
    test_log()
