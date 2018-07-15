# 2017/02/18
# 作业 2
# ========
#
#
# 请直接在我的代码中更改/添加, 不要新建别的文件
from client_ssl import get


# 定义我们的 log 函数
def log(*args, **kwargs):
    print(*args, **kwargs)


# 作业 2.1
#
# 实现函数
def path_with_query(path, query):
    '''
    path 是一个字符串
    query 是一个字典

    返回一个拼接后的 url
    详情请看下方测试函数
    '''
    pass


def test_path_with_query():
    # 注意 height 是一个数字
    path = '/'
    query = {
        'name': 'gua',
        'height': 169,
    }
    expected = [
        '/?name=gua&height=169',
        '/?height=169&name=gua',
    ]
    # NOTE, 字典是无序的, 不知道哪个参数在前面, 所以这样测试
    assert path_with_query(path, query) in expected


# 作业 2.2
#
# 为作业1 的 get 函数增加一个参数 query
# query 是字典


# 作业 2.3
#
# 实现函数
def header_from_dict(headers):
    '''
    headers 是一个字典
    范例如下
    对于
    {
    	'Content-Type': 'text/html',
        'Content-Length': 127,
    }
    返回如下 str
    'Content-Type: text/html\r\nContent-Length: 127\r\n'
    '''
    pass


# 作业 2.4
#
# 为作业 2.3 写测试


# 作业 2.5
#
"""
豆瓣电影 Top250 页面链接如下
https://movie.douban.com/top250
我们的 client_ssl.py 已经可以获取 https 的内容了
这页一共有 25 个条目

所以现在的程序就只剩下了解析 HTML

请观察页面的规律，解析出
1，电影名
2，分数
3，评价人数
4，引用语（比如第一部肖申克的救赎中的「希望让人自由。」）

解析方式可以用任意手段，如果你没有想法，用字符串查找匹配比较好(find 特征字符串加切片)
"""


def find2(s1, s2):
    """
    s1 s2 都是 str
    两个 str 的长度不限

    返回 s2 在 s1 中的下标, 从 0 开始, 如果不存在则返回 -1
    """
    len1 = len(s1)
    len2 = len(s2)
    result = -1
    i = 0
    while (i + len2) < len1 + 1:
        sa = s1[i:(i + len2)]
        if s2 != sa:
            i = i + 1
            continue
        else:
            if result > 0:
                i = i + 1
                continue
            else:
                result = i
                # log("resul s", result)
        i = i + 1
    return result


def find_between(s, left, right):
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
    # left = '#<'
    # right = '>#'
    str = s
    lef = left
    rig = right
    le = -1
    ri = -1
    result = 'find null'
    # 匹配第一个字符串的位置
    # find2(str, rig)
    le = find2(str, lef) + len(lef)
    # print("le", le)
    # 切右边的字符串, 找第一匹配的右字符
    ris = le + 30
    rstr = str[le: ris]
    ri = find2(rstr, rig)
    # 剩下的部分为 str = str[le + ri:]
    # print("ri")
    result = rstr[0:ri]
    i = 0
    rs = [result]
    # log('result', result)
    # log('i', i)
    i = i + 1
    while i < 100:
        str = str[le + ri:]
        le = find2(str, lef) + len(lef)
        # 切右边的字符串, 找第一匹配的右字符
        ris = le + 30
        rstr = str[le: ris]
        # log("inner right str", rstr)
        ri = find2(rstr, rig)
        # 剩下的部分为 str = str[le + ri:]
        result = rstr[0:ri]
        i = i + 1
        if '&nbsp' in result:
            continue
        else:
            rs.append(result)
        # log("inner rs", rs)
    return rs


def find_element_by_label(body, left_label, right_label):
    # left = '<span class="title">'
    # right = '</span>'
    # left = left_label
    # right = right_label
    # element = find_between(body, left, right)
    now_str = body

    # 做多少次循环呢
    # 统计body里面左边字符串出现的次数
    # 并且加入到elements里面
    elements = []
    i = 0
    n = now_str.count(left_label)

    while i < n:
        left = now_str.find(left_label) + len(left_label)
        now_str = now_str[left:]
        right_str = now_str[:60]
        right = right_str.find(right_label)
        # log("right_str", right_str, i)
        # log("inner left_label right label\n", left_label, right_label)
        if right != -1:
            # now_str = now_str[left:]
            e = now_str[:right]
            # log("inner ({}), i".format(e, i))
            if '&nbsp' in e:
                i = i + 1
                # log("&nbsp,", e)
                continue
            else:
                elements.append(e)
        else:
            # log("lcontinue,", i, right)
            i += 1
            continue
        i += 1
        # log("left, right,", left, right)
        # log("right str,", right_str)
        # log("次数", n)
        # log("element eles len(lens)", e, elements, len(elements))
    # 先找到标签左边的坐标
    # 找到右边标签的坐标
    # left_position = left + len(left)
    #
    # 字符串 element = nor_str[]
    # log("element eles len(lens)", e, elements, len(elements))
    log("len ", len(elements))
    return elements


def parsed_html(url):
    # 接收一个网址
    # 返回解析出的
    # 1，电影名  <span class="title">这个杀手不太冷</span>
    # 2，分数   <span class="rating_num" property="v:average">9.4</span>
    # 3，评价人数  <span>994476人评价</span>
    # 4，介绍 <span class="inq">怪蜀黍和小萝莉不得不说的故事。</span>
    # 标签找到元素
    url = 'https://movie.douban.com/top250?start=25'
    status_code, headers, body = get(url)
    movies_labels = ['<span class="title">', '</span>']
    sorces_labels = ['<span class="rating_num" property="v:average">', '</span>']
    coments_labels = ['<span>', '人评价</span>']
    inqs_labels = ['<span class="inq">', '</span>']

    movies = find_element_by_label(body, movies_labels[0], movies_labels[1])
    sorces = find_element_by_label(body, sorces_labels[0], sorces_labels[1])
    coments = find_element_by_label(body, coments_labels[0], coments_labels[1])
    inqs = find_element_by_label(body, inqs_labels[0], inqs_labels[1])
    result = [1] * len(movies)

    for i in range(len(movies)):
        m = movies[i]
        s = sorces[i]
        c = coments[i]
        ins = inqs[i]
        op = '\n'
        # log("movies ({}), ({}))".format(ins, i))
        res = m + op + s + op + c + op + ins + op
        result[i] = res
        # log("res\n", res, i)
    # log("result ({}),\n url =({})".format(result, url))

    return result


def test_find_element_by_label():
    url = 'http://movie.douban.com/top250'
    status_code, headers, body = get(url)
    test_items = [
        #   ('<a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 5.0 全新发布</a>', ("</a>")),
        ('<span class="title">', ('</span>')),
        #   ('<span class="title">肖申克的救赎', ("</span>")),
    ]
    # test_function = find_element_by_label
    # left = now_str.find(left_label) + len(left_label)
    # right = now_str.find(right_label)
    # test_function_name = test_function.__name__
    for t in test_items:
        log("t", t)
        left_label, right_label = t
        find_element_by_label(body, left_label, right_label)


def test_parsed_html():
    url = 'http://movie.douban.com/top250'
    parsed_html(url)


def test_find_between():
    url = 'http://movie.douban.com/top250'
    status_code, headers, body = get(url)
    content = body
    left = '<span class="title">'
    right = '</span>'
    left1 = '<span class="rating_num" property="v:average">'
    # print("contens", content )
    content1 = find_between(content, left, right)
    content2 = find_between(content, left1, right)
    print('结果1 ', content1)
    # print('结果2 ', content2)


# 作业 2.6
#
"""
通过在浏览器页面中访问 豆瓣电影 top250 可以发现
1, 每页 25 个条目
2, 下一页的 URL 如下
https://movie.douban.com/top250?start=25

因此可以用循环爬出豆瓣 top250 的所有网页

于是就有了豆瓣电影 top250 的所有网页

由于这 10 个页面都是一样的结构，所以我们只要能解析其中一个页面就能循环得到所有信息

所以现在的程序就只剩下了解析 HTML

请观察规律，解析出
1，电影名
2，分数
3，评价人数
4，引用语（比如第一部肖申克的救赎中的「希望让人自由。」）

解析方式可以用任意手段，如果你没有想法，用字符串查找匹配比较好(find 特征字符串加切片)
"""


def parsed_all_html(n):
    # 传入一个数字
    # 返回所有的
    # 每一页25个元素
    url = 'https://movie.douban.com/top250?start='
    now_url = url
    n = 250
    i = 0
    while i < 6:
        rs = parsed_html(now_url)
        now_url = url + str(25 * i)
        log("第({})个, 长度({}),now_url =({})".format(i, len(rs), now_url))
        log("rs".format(rs))
        i += 1


def test_parsed_all_html():
    parsed_all_html(250)


# 单元测试
def test():
    # test_find_between()
    # test_find_element_by_label()
    # test_parsed_html()
    test_parsed_all_html()


def main():
    s = 'sss'


if __name__ == '__main__':
    # main()
    test()
