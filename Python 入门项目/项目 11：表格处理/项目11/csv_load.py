import csv
import time


def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)


def load_csv():
    filename = '11-info.csv'
    # filename = 'test-info.csv'
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        log('header_row({})'.format(header_row))
        # for row in reader:
        #     log('all({}) type({})'.format(row, type(row)))
        lines = []
        for order_num, trade_name, producer, price in reader:

            # 初始化line 每次的line不一样
            line = [1] * 4
            t = order_num, trade_name, producer, price
            print('before line({})', line)
            # 将当前数据赋值给 line
            for i in range(len(t)):
                line[i] = t[i]
            # log("after line({}) i =({})".format(line))
            print('after line({})', line)
            # 将line添加到lines里面去
            lines.append(line)
            print('line', hex(id(line)))
            log("now lines({}) len lines =({})".format(lines, len(lines)))

    log('lines({})'.format(lines))
    return lines


def write_csv():
    # 接收一个数组
    datas = [['name', 'age'],
             ['Bob', 14],
             ['Tom', 23],
             ['Jerry', '18']]
    filename = 'test-info.csv'
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        # newline=''如果不写这个属性 默认为写入的数据空一行
        writer = csv.writer(f)
        for row in datas:
            writer.writerow(row)


def fin_physical_address(obj):
    # 传入对象
    # 返回获取对象地址

    return hex(id(obj))


if __name__ == '__main__':
    load_csv()
    # write_csv()

