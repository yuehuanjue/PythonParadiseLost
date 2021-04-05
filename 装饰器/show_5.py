# @dese: 这是总结 python 装饰器用法的地方 -- 装饰类的装饰器
# @date: 2021/04/05
# @author：小十二


"""
装饰类的装饰器


比如单例模式的一种写法

"""

instances = {}


def singleton(cls):
    def get_instance(*args, **kw):
        cls_name = cls.__name__

        print('===== 1 ====')
        if not cls_name in instances:
            print('===== 2 ====')
            instance = cls(*args, **kw)
            instances[cls_name] = instance
        return instances[cls_name]

    return get_instance


@singleton
class User:
    _instance = None

    def __init__(self, name):
        print('===== 3 ====')

        self.name = name

u1 = User("Sum")
u1.age = 20
u2 = User("Huan")
assert (u1 is u2)

# >>> u1 = User("Sum")
# ===== 1 ====
# ===== 2 ====
# ===== 3 ====
# >>> u1.age = 20
# >>> u2 = User("Huan")
# ===== 1 ====
# >>> u2.age
# 20
# >>> u1 is u2
# True
