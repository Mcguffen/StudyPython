import json
from routes.session import session
from utils import (
    log,
    redirect,
    http_response,
    json_response,
)
from models.todo import Todo
from models.weibo import Weibo


def all_weibo(request):
    """
    返回所有 todo
    """
    ms = Weibo.all()
    # 要转换为 dict 格式才行
    data = [m.json() for m in ms]
    return json_response(data)


def add_weibo(request):
    """
    接受浏览器发过来的添加 weibo 请求
    添加数据并返回给浏览器
    """
    log('后端接收到的前端数据', )
    form = request.json()
    log('接收到的前端的数据', form)
    # 创建一个 model
    m = Weibo.new(form)
    log('创建的微博对象', m)
    # 把创建好的 model 返回给浏览器
    return json_response(m.json())


def delete_weibo(request):
    """
    通过下面这样的链接来删除一个 todo
    /delete?id=1
    """
    weibo_id = int(request.query.get('id'))
    t = Weibo.delete(weibo_id)
    return json_response(t.json())


def update_weibo(request):
    # 更新微博
    log('路由到了更新微博')
    form = request.json()
    weibo_id = int(form.get('id'))
    log('debug 更新*****({} form({}))'.format(weibo_id, form))
    t = Weibo.update(weibo_id, form)
    log('更新微博({})'.format(t))
    return json_response(t.json())


route_dict = {
    # weibo api
    '/api/weibo/all': all_weibo,
    '/api/weibo/add': add_weibo,
    '/api/weibo/delete': delete_weibo,
    '/api/weibo/update': update_weibo,
}
