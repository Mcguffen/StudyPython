import json
# from utils.log import log



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
        # log('load', s)
        return json.loads(s)


def numbers_to_josn():
    number = []

    # 包含100数字的数组
    for i in range(1000):
        number.append(i)

    filename = 'numbers.json'

    save(number, filename)


def load_json_numbers():
    filename = 'numbers.json'

    numbers = load(filename)

    print(type(numbers[1]), numbers)


def test():
    numbers_to_josn()
    load_json_numbers()
    # load('number.json')
    pass


if __name__ == '__main__':
    test()
    # log("嘻嘻")
