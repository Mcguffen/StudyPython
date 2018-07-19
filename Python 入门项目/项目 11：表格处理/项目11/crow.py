# 这是一个解析网页基础的爬虫
# 我写的函数在第一个
import urllib.request
import time
import json
from utils import log
from csv_load import load_csv


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
        log('load', s)
        return json.loads(s)


def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)


def find_between_label(s, left_label, right_label, bytelen=30):
    """
    s, left, right 都是 str
    具体用法参考下方的代码
    """
    # 1, 观察用法可以知道本函数的功能就是把 left 和 right 之间包含的字符串提取出来
    # 2, 为了实现这个目的, 我们的想法应该是拿到 目标字符串 的开始和结束下标, 然后用 切片 的方式提取
    # 3, 我们先定位到 left 的下标(使用 find2 函数), 加上 left 的长度就可以得到结果的开始下标(具体你要通过 log 的方式来尝试, 纸笔计算好)
    # 4, 我们再定位到 right 的下标, 就可以切片出目标字符串
    # 5, 返回目标字符串
    # ps; 先找到左边的再匹配右边的
    log('start  find_between_label')

    now_lines = s
    bt_len = bytelen

    # 查找当前页面一共有多少需要解析的元素 以左标签为参数
    # 一次取出要解析的元素 放到rs 数组中
    num = s.count(left_label)
    i = 0
    rs = []
    while i < num:
        # 匹配第一个字符串的位置left position
        left_position = now_lines.find(left_label) + len(left_label)
        # 切割 出需要 包含解析元素 和left label位置的字符串
        len_byts = left_position + bt_len
        # 切割出字符串
        now_str = now_lines[left_position:len_byts]
        right_position = now_str.find(right_label)
        # 切割出需要的元素
        line = now_str[:right_position]
        # 剩下的字符串为 now_lines
        now_lines = now_lines[left_position + right_position:]
        rs.append(line)

        i += 1
        # log("i = ({})".format(i))
    log('end  find_between_label')
    return rs


def openurl(url):
    log('start  openurl')
    # url = 'https://movie.douban.com/top250'
    # 下载页面, 得到的是一个 bytes 类型的变量 s
    s = urllib.request.urlopen(url).read()
    # 用 utf-8 编码把 s 转为字符串并返回
    content = s.decode('utf-8')
    log('end  openurl')
    return content


def array_to_dict(array):
    log('start  array_to_dict')
    # 接收数组
    # ['110000', '北京市', '110101', '东城区', ]
    # 返回dict = {
    #   '北京市' : '110000' ,
    #   '东城区' : '110101' ,
    # }
    dic = {}
    if array is None:
        return dic
    lens = len(array)

    # 如果lens为奇数 进行出错处理

    # 取出当前数组的值
    # 偶数为key 奇数为value

    i = 0
    while i < lens:
        k = array[i + 1]
        v = array[i]
        dic[k] = v
        i += 2

    log('len dic = ({})'.format(len(dic)))
    log('end  array_to_dict')
    # 保存dic文件
    save(dic, 'info-dict.txt')
    return dic


def test_array_to_dict():
    # log('start  test_find_between_label')
    url = 'http://www.mca.gov.cn/article/sj/tjbz/a/2017/201801/201801151447.html'
    body = openurl(url)
    left = '<td class=xl7026226>'
    right = '</td>'
    # log('start find_between_label')
    res = find_between_label(body, left, right)
    # log('after find_between_label')
    dic = array_to_dict(res)
    # log('end')
    k1 = '北京市'
    k2 = '东城区'

    log('debug len dic({}) 东城区 =({}) 北京市= ({})'.format(len(dic), dic[k2], dic[k1]))
    # log('end  test_find_between_label')
    pass


def find_province_by_name():
    # 接收区名
    # 返回上一级的省名

    pass


def test_find_between_label():
    log('start  test_find_between_label')
    url = 'http://www.mca.gov.cn/article/sj/tjbz/a/2017/201801/201801151447.html'
    body = openurl(url)
    left = '<td class=xl7026226>'
    right = '</td>'
    res = find_between_label(body, left, right)
    print('debug res', res)
    log('end  test_find_between_label')
    pass


def test():
    # test_find_between_label()
    # log('start test')
    test_array_to_dict()
    # log('end test')
    pass


if __name__ == '__main__':
    test()
