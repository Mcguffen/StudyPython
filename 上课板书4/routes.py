from utils import log
from models import Message
from models import User

import random


# 这个函数用来保存所有的 messages
message_list = []
# session 可以在服务器端实现过期功能
session = {
    'session id': {
        'username': 'gua',
        '过期时间': '2.22 21:00:00'
    },
    'user_id': 0,
}


def random_str():
    """
    生成一个随机的字符串
    """
    seed = 'abcdefjsad89234hdsfkljasdkjghigaksldf89weru'
    s = ''
    for i in range(16):
        # 这里 len(seed) - 2 是因为我懒得去翻文档来确定边界了
        random_index = random.randint(0, len(seed) - 2)
        s += seed[random_index]
    return s


def template(name):
    """
    根据名字读取 templates 文件夹里的一个文件并返回
    """
    path = 'templates/' + name
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def current_user(request):
    session_id = request.cookies.get('user', '')
    username = session.get(session_id, '【游客】')
    # username = request.cookies.get('user', '【游客】')
    return username


def get_user_by_session(request):

    pass


def route_index(request):
    """
    主页的处理函数, 返回主页的响应
    """
    header = 'HTTP/1.1 210 VERY OK\r\nContent-Type: text/html\r\n'
    body = template('index.html')
    username = current_user(request)
    body = body.replace('{{username}}', username)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def response_with_headers(headers):
    """
Content-Type: text/html
Set-Cookie: user=gua
    """
    header = 'HTTP/1.1 210 VERY OK\r\n'
    header += ''.join(['{}: {}\r\n'.format(k, v)
                           for k, v in headers.items()])
    return header


def route_login(request):
    """
    登录页面的路由函数
    """
    headers = {
        'Content-Type': 'text/html',
        # 'Set-Cookie': 'height=169; gua=1; pwd=2; Path=/',
    }
    # log('login, headers', request.headers)
    log('login, cookies', request.cookies)
    username = current_user(request)
    if request.method == 'POST':
        form = request.form()
        u = User.new(form)
        # log('bebug*** login user profile({})'.format(u))
        if u.validate_login():
            # 设置一个随机字符串来当令牌使用
            # 根据用户名和密码查用户id
            log('bebug*** login user validate_login({})'.format(u.password))
            now_user = User.find_by(password=u.password)
            # log('bebug*** after login user ({})'.format(now_user))
            # 在session里面设置用户id
            session_id = random_str()
            session[session_id] = u.username
            session['user_id'] = now_user.id
            # log('seesion usr_id({})'.format(session.get('user_id', '')))
            headers['Set-Cookie'] = 'user={}'.format(session_id)
            # 下面是把用户名存入 cookie 中
            # headers['Set-Cookie'] = 'user={}'.format(u.username)
            result = '登录成功'

            # 跳转到profile
            log('request', request)
            rs = route_profile(request)
            return rs

        else:
            result = '用户名或者密码错误'
    else:
        result = ''
    body = template('login.html')
    body = body.replace('{{result}}', result)
    body = body.replace('{{username}}', username)
    log('username({})'.format(username))
    header = response_with_headers(headers)
    r = header + '\r\n' + body
    log('login 的响应', r)
    return r.encode(encoding='utf-8')


def route_register(request):
    """
    注册页面的路由函数
    """
    header = 'HTTP/1.x 210 VERY OK\r\nContent-Type: text/html\r\n'
    if request.method == 'POST':
        form = request.form()
        u = User.new(form)
        log('form({}) u = ({})'.format(form, u))
        if u.validate_register():
            u.save()
            log('user save({})'.format(u))
            result = '注册成功<br> <pre>{}</pre>'.format(User.all())
        else:
            log("test save".format(u))
            result = '用户名或者密码长度必须大于2'
    else:
        result = ''
    body = template('register.html')
    body = body.replace('{{result}}', result)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def route_message(request):
    """
    消息页面的路由函数
    """
    username = current_user(request)
    if username == '【游客】':
        log("**debug, route msg 未登录")
        pass
    log('本次请求的 method', request.method)
    if request.method == 'POST':
        form = request.form()
        msg = Message.new(form)
        log('post', form)
        message_list.append(msg)
        # 应该在这里保存 message_list
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    # body = '<h1>消息版</h1>'
    body = template('html_basic.html')
    msgs = '<br>'.join([str(m) for m in message_list])
    body = body.replace('{{messages}}', msgs)
    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')


def route_static(request):
    """
    静态资源的处理函数, 读取图片并生成响应返回
    """
    filename = request.query.get('file', 'doge.gif')
    path = 'static/' + filename
    with open(path, 'rb') as f:
        header = b'HTTP/1.x 200 OK\r\nContent-Type: image/gif\r\n\r\n'
        img = header + f.read()
        return img


def route_profile(request):
    """
    消息页面的路由函数
    """
    log('inner profile({})'.format(request))
    # username = current_user(request)
    # log("session username({})".format(session.get('session id').get('username')))
    username = session.get('session id').get('username')
    log("session({})".format(session))
    if username == '【游客】':
        # # 如果没登录, 返回 302 为状态码来 重定向到登录界面
        # # 当返回 302 响应的时候, 必须在 HTTP 头部加一个 Location 字段并且设置值为你想要定向的页面
        log("**debug, route profile 未登录")
        header = 'HTTP/1.1 302 Moved Momently\r\nContent-Type: text/html\r\nLocation: http://localhost:3000\r\n'
        # 好吧只返回header
        # body = template('login.html')
        # body.replace('{{username}}', username)
        body = template('302_status.html')
        pass
    else:
        #
        user_id = session.get('user_id')
        now_user = User.find_by(id=user_id)
        # 登录了之后跳转到profile页面
        log("***debug , route profile 已登录用户({})".format(now_user))
        # 根据用户名获取用户
        # username userid usernote 可以用函数处理
        #

        header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
        # body = '<h1>消息版</h1>'
        body = template('profile.html')
        # msgs = '<br>'.join([str(m) for m in message_list])
        body = body.replace('{{username}}', now_user.username)
        body = body.replace('{{userid}}', str(now_user.id))
        #
        log("now_user.note({})".format(now_user.note))
        body = body.replace('{{usernote}}', str(now_user.note))

    r = header + '\r\n' + body
    return r.encode(encoding='utf-8')

    pass
# 路由字典
# key 是路由(路由就是 path)
# value 是路由处理函数(就是响应)


route_dict = {
    '/': route_index,
    '/login': route_login,
    '/register': route_register,
    '/messages': route_message,
    '/profile': route_profile,
}


def test_route_profile():
    route_profile()
    pass


def test():
    pass


if __name__ == '__main__':
    test()