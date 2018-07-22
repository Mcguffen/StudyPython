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


def find_value_by_code(code):
    # 接受一个code
    # 返回对应的字符串
    path = 'info-dict.txt'
    info_dict = load(path)

    for k, v in info_dict.items():
        key, value = k, v
        # log('key****({}) value({}) '.format(key, value))
        if key is None:
            break

        if key == code:
            # log('key**** ', key)
            return value
    # value = info_dict.get(code)
    # log('key', k, v, code)

    return key


def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]


def find_code_by_value(supple_name):
    borough_supple = ['区', '县', '市', '省']
    info_dict = load('info-dict.txt')

    #  例如 陕西  "陕西省": "610000",
    #  返回 陕西省, 返回610000 否则返回none
    supple_name = '陕西'

    i = 0
    while i < len(borough_supple):
        supple_ed_name = supple_name + str(borough_supple[i])
        need_value = ''
        codes = get_key(info_dict, supple_ed_name)
        log('codes({})'.format(codes))
        # for k, v in info_dict.items():
        #     key, value = k, v
        #     if supple_ed_name == value:
        #         log('k ({}) v({}) supple_ed_name({})'.format(k, v, supple_ed_name))
        #         need_value = key

        if need_value is None:
            i = i + 1
            continue

        else:
            # log('code### ', code, i)
            return need_value
    return None


def code_with_none(supple_name):
    # 接受一个字符 返回处理后的字符
    # 例如 山西
    # 返回 山西省
    # info_dict = load('info-dict.txt')
    borough_supple = ['区', '县', '市', '省']
    info_dict = load('info-dict.txt')

    #  例如 陕西  "陕西省": "610000",
    #  返回 陕西省, 返回610000 否则返回none
    i = 0
    while i < len(borough_supple):
        supple_ed_name = supple_name + str(borough_supple[i])
        #
        keys = get_key(info_dict, supple_ed_name)
        log('keys = ({})'.format(keys))

        # 如果没找到
        if keys is None:
            i = i + 1
            continue
        else:
            return keys

        i = i + 1

    log('keys end', keys, i)
    return None


def find_borough_code(borough_name):
    # 根据传入的行政区名字
    # 返回行政代码
    # 如果是 陕西 返回 陕西省 的区域代码
    name = borough_name
    # name = '陕西'

    # 如果数据 陕西 补足为  陕西区 省 市 .. 查找行政代码
    # 如果没有 返回错误信息
    info_dict = load('info-dict.txt')
    code = info_dict.get(name)
    if code is None:
        code = code_with_none(name)
        log('time({})'.format(code))
    # log('code({}) find_borough_code)'.format(code))

    return code


def find_borough_name(borough):
    # 传入行政区名字 例如 深圳 或深圳市
    # 查询行政代码
    # 返回当前省名
    ten_thousand = 10000
    local_proceder = borough
    code = find_borough_code(local_proceder)
    # code = int(code)

    # 根据行政code 识别本省的 行政code
    # province_code = int(code / ten_thousand) * ten_thousand
    # province = find_value_by_code(province_code)
    # log('debug find_borough_name', code, type(ten_thousand), province_code, province)

    # return province


def add_new_colum(file, new_colum):
    # 接收文件, 要添加的字段
    # 返回添加字段之后的文件
    lines = load_csv(file)
    informations = []
    new_colum = '产地(省)'
    # 将给数据添加新的字段 '产地（省）' 并且赋值
    for i in range(len(lines)):
        header = lines[i]
        now_colum = []
        order_num, trade_name, producer, price = lines[i]
        # 将给数据添加新的字段 '产地（省）'
        if i == 0:
            producer_province = new_colum
            pass
        else:
            producer_province = find_borough_name(producer)
        # log('producer({}),producer_province ({})  i = ({})'.format(producer, producer_province, i))
        # 给新的字段添加数据
        h = order_num, trade_name, producer_province, producer, price
        for item in h:
            now_colum.append(item)
            # log('headers=({})'.format(now_colum))
        # 将添加后的数据加到informations数组中
        informations.append(now_colum)
    log('len add_new_colum({})'.format(len(informations)))

    return informations
    pass


def find_code_by_borough_name():
    # 已经得到json化的行政区 --区代码的文件
    # 需要得到csv文件转化的的数组
    # 保存到'after-11-info.csv'文件中
    file_name = 'test-after-11-info.csv'
    new_colum = '产地(省)'
    informations = add_new_colum(file_name, new_colum)
    # 将复制后的数据存到csv文件中去
    write_csv(informations, file_name)
    pass


def test_find_borough_code():
    # name = '陕西省'
    name1 = '陕西'
    # find_borough_code(name)
    # find_borough_name(name1)
    # find_borough_code(name1)
    find_code_by_borough_name()


def test():
    # find_code_by_borough_name()
    test_find_borough_code()
    pass


def main():

    pass


if __name__ == '__main__':
    test()
    # main()
