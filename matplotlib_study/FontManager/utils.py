# 这是一个工具类
# 包含断点调试的基本模版
import time


def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)


def ensure(condition, message):
    # 在条件不成立的时候, 输出 message
    if not condition:
        log('*** 测试失败:', message)
    else:
        log("测试成功")


# 这是测试功能函数
def test_function_with_name():
    '''

    :return:

    测试该功能
    传入的value, 希望得到的是expected

    '''
    # fun_value 是一个函数, 测试条件与结果可以写成一个字典
    # 传入一个测试函数fun_value, 以及测试条件
    fun_value = 'function'
    value = {
        'Content-Type': 'text/html',
        'Content-Length': 127,
    }
    # test_function.__name__

    excepted = "Content-Type:text/html\r\nContent-Length:127\r\n"
    test_function = fun_value
    test_function_name = test_function.__name__
    test_items = [
        (value, (excepted)),
    ]

    for t in test_items:
        value, expected = t
        u = test_function(value)
        # assert 是一个语句, 名字叫 断言
        # 如果断言成功, 条件成立, 则通过测试
        # 否则为测试失败, 中断程序报错
        # funtion 写自己写的函数的名称
        e = "{} ERROR, ({}) ({}) ({})".format(test_function_name, value, u, expected)
        ensure(u == expected, e)
        assert u == expected, e
        log('***********************  {}}  测试完成'.format(test_function_name))
