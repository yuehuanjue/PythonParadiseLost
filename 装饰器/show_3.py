# @dese: 这是总结 python 装饰器用法的地方 -- 函数 + 类
# @date: 2021/04/05
# @author：小十二


# 函数装饰器 + 类

# 一、 让装饰器带 类 参数
class mylocker:
    def __init__(self):
        print("mylocker.__init__() called.")

    @staticmethod
    def acquire():
        print("mylocker.acquire() called.")

    @staticmethod
    def unlock():
        print("  mylocker.unlock() called.")


class lockerex(mylocker):
    @staticmethod
    def acquire():
        print("lockerex.acquire() called.")

    @staticmethod
    def unlock():
        print("  lockerex.unlock() called.")


def lockhelper(cls):
    '''cls 必须实现acquire和release静态方法'''

    def _deco(func):
        def __deco(*args, **kwargs):
            print("before %s called." % func.__name__)
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()

        return __deco

    return _deco


class example:
    @lockhelper(mylocker)
    def myfunc(self):
        print(" myfunc() called.")

    @lockhelper(mylocker)
    @lockhelper(lockerex)
    def myfunc2(self, a, b):
        print(" myfunc2() called.")
        return a + b


a = example()
a.myfunc()
print(a.myfunc())
print(a.myfunc2(1, 2))
print(a.myfunc2(3, 4))
