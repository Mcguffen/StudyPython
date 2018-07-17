import json

from utils import log


def save(data, path):
    """
    本函数把一个 dict 或者 list 写入文件
    data 是 dict 或者 list
    path 是保存文件的路径
    """
    # json 是一个序列化/反序列化(上课会讲这两个名词) list/dict 的库
    # indent 是缩进
    # ensure_ascii=False 用于保存中文
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
        log('save', path, s, data)
        f.write(s)


def load(path):
    """
    本函数从一个文件中载入数据并转化为 dict 或者 list
    path 是保存文件的路径
    """
    with open(path, 'r', encoding='utf-8') as f:
        s = f.read()
        log('load', s)
        return json.loads(s)


# Model 是用于存储数据的基类
class Model(object):
    # @classmethod 说明这是一个 类方法
    # 类方法的调用方式是  类名.类方法()
    @classmethod
    def db_path(cls):
        # classmethod 有一个参数是 class
        # 所以我们可以得到 class 的名字
        classname = cls.__name__
        path = '{}.txt'.format(classname)
        return path

    @classmethod
    def new(cls, form):
        m = cls(form)
        return m

    @classmethod
    def all(cls):
        """
        得到一个类的所有存储的实例
        """
        path = cls.db_path()
        models = load(path)
        ms = [cls.new(m) for m in models]
        return ms

    def save(self):
        """
        save 函数用于把一个 Model 的实例保存到文件中
        """
        models = self.all()
        log('models', models)
        models.append(self)
        # __dict__ 是包含了对象所有属性和值的字典
        l = [m.__dict__ for m in models]
        path = self.db_path()
        save(l, path)

    def __repr__(self):
        """
        这是一个 魔法函数
        不明白就看书或者 搜
        """
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '< {}\n{} >\n'.format(classname, s)


# 以下两个类用于实际的数据处理
# 因为继承了 Model
# 所以可以直接 save load
class User(Model):
    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')

    def validate_login(self):
        # 获取用户名和密码

        # 从数据库取出数据
        all = User.all()
        stuats = False
        # 循环对比用户
        # 用户名密码一样的话 返回用户名和密码
        for i in range(len(all)):
            now_user = all[i]
            # log("self({}), now user({}),self == now_user?({}) ".format(self, now_user, self == now_user))
            # return self == now_user
            if self.username == now_user.username:
                if self.password == now_user.password:
                    stuats = True
            else:
                stuats = False
            # log("self({}), now user({}),\nstuats?({}), i ({})\n\n".format(self, now_user, stuats, i))
            # 当前stutas 为True 时候 跳出循环
            if stuats == True:
                break

        return stuats
        # return self.username == 'gua' and self.password == '123'

    def validate_register(self):
        return len(self.username) > 2 and len(self.password) > 2


# 定义一个 class 用于保存 message
class Message(Model):
    def __init__(self, form):
        self.author = form.get('author', '')
        self.message = form.get('message', '')


def test_user():
    all = User.all()
    test_user = all[3]
    p = test_user.password
    n = test_user.username
    log(" login({})".format(test_user.validate_login()))
    # log("all user({}), type of inner({}),len all({})".format(all, type(test_u), len(all)), p, n)
    pass


def test():
    test_user()
    pass


if __name__ == '__main__':
    test()
