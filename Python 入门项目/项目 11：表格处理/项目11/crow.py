# 这是一个解析网页基础的爬虫
import urllib.request
from utils import log

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
    # print("rstr", rstr)
    ri = find2(rstr, rig)
    # 剩下的部分为 str = str[le + ri:]
    # print("ri")
    result = rstr[0:ri]
    i = 0
    rs = [result]
    # log('result', result)
    log('i', i)
    i = i + 1
    while i < 25:
        str = str[le + ri:]
        # log('result', result)
        # log('i', i)
        le = find2(str, lef) + len(lef)
        # 切右边的字符串, 找第一匹配的右字符
        ris = le + 30
        rstr = str[le: ris]
        ri = find2(rstr, rig)
        # 剩下的部分为 str = str[le + ri:]
        result = rstr[0:ri]
        i = i + 1
        rs.append(result)
    # print("rs", rs)
    return rs


def openurl(url):
    # 这里把 url 写死为豆瓣 top250 页面
    url = 'https://movie.douban.com/top250'
    # 下载页面, 得到的是一个 bytes 类型的变量 s
    s = urllib.request.urlopen(url).read()
    # 用 utf-8 编码把 s 转为字符串并返回
    content = s.decode('utf-8')
    return content