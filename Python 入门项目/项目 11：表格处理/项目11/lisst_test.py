# c测试列表
from utils import log


def testlist():

    list1 =[]
    a = ['100', '键盘', '忻府区', '80']
    list1.append(a)
    list1.append('ccc')

    log('debug list({})'.format(list1))


if __name__ == '__main__':
    testlist()