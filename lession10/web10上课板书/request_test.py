
def request_test():

    r = 'GET /api/weibo/all HTTP/1.1'
    r = 'xiao bai tulalalal'
    path = r.split()[1]
    method = r.split()[0]
    print('path =({}), method = ({}) r.splite = ({})'.format( path, method, r.split('i')))


if __name__ == '__main__':
    request_test()

