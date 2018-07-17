from utils import log

def test_kv():
    nowstr = 'username-localhost-8888="2|1:0|10:1529983402|23:username-localhost-8888|44:NTA1YzQ2YTQyNjcwNGY3ODgyNDhmMzk0MGYwMDYzMzQ=|e4a0cd21e6bcb15cc521249132ac05514ce7da13f184396bf0533c59e'
    k, v = nowstr.split(":", 1)
    log("k v \n type", k, type(k), v, len(k))


def test():
    test_kv()


if __name__ == '__main__':
    test()