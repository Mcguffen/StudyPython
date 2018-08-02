from models import Model
import time


class Td(Model):
    @classmethod
    def new(cls, form):
        """
        创建并保存一个 Td 并且返回它
        Td.new({'title': '吃饭'})
        :param form: 一个字典 包含了 Td 的数据
        :return: 创建的 Td 实例
        td.txt 为空时候 --> 包含 '[]'
        """
        # 下面一行相当于 t = Todo(form)
        t = cls(form)
        t.save()
        return t

    def __init__(self, form):
        self.id = None
        self.td = form.get('td', '')
        self.list_rD = form.get('list_rD', '')
        self.list_TD = form.get('list_TD', '')
        self.create_time = int(time.time())


