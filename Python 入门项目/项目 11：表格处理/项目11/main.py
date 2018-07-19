from crow import find_between_label
from csv_load import *
from utils import log
import json


def save(data, path):
    """
    data 是 dict 或者 list
    path 是保存文件的路径
    """
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
        # log('save', path, s, data)
        f.write(s)


def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        # log('debug  load', s)
        return json.loads(s)


def find_borough_code(borough_name):
    # 根据传入的行政区名字
    # 返回行政代码
    code = None
    name = borough_name
    name = '陕西'
    # 如果数据 陕西 补足为  陕西区 省 市 .. 查找行政代码
    # 如果没有 返回错误信息
    borough_supple = ['区', '县', '市', '省']
    info_dict = load('info-dict.txt')

    # for i in borough_name:
    #     if borough_name[i] in name:
    #         pass
    # t.get('d')
    code = info_dict.get(name)
    if code is None:

        log('time')
    log('code({})'.format(code))
    pass


def find_borough_name(borough):
    # 传入行政区名字 例如 深圳 或深圳市
    # 查询行政代码
    # 返回当前省名
    province = borough
    # if province is not None:
    #     pass
    # else:
    #     return None



    pass


def find_code_by_borough_name():
    # 已经得到json化的行政区 --区代码的文件
    # 需要得到csv文件转化的的数组
    lines = load_csv()
    log('lines 1 ({})'.format(lines[0]))

    for i in range(len(lines)):
        if i == 0:
            producer_province = '产地（省）'
            pass
        else:
            producer_province = find_borough_name()
    # 给lines数组添加值
    header = lines[i]
    order_num, trade_name, producer, price = lines[i]
    # log('order_num=({}),trade_name({}),producer({}),price({})'.format(order_num, trade_name, producer, price))
    producer_province = '产地（省）'
    # 在字符头添加producer_province字段
    headers = []
    h = order_num, trade_name,producer_province, producer, price
    for item in h:
        headers.append(item)
        log('headers=({})'.format(headers))


    pass


def test_find_borough_code():
    name = '陕西省'
    # name1 = '陕西'
    find_borough_code(name)
    # find_borough_code(name1)


def test():
    # find_code_by_borough_name()
    test_find_borough_code()
    pass


def main():

    pass


if __name__ == '__main__':
    test()
    # main()
