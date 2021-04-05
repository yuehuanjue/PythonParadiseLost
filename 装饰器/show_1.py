# @dese: 这是总结 python 装饰器用法的地方 -- 函数装饰器
# @date: 2021/04/05
# @author：小十二


# 函数装饰器

# 一、 简单装饰器
import time


def timeit(func):
    def result():
        start_time = time.time()
        func()
        end_time = time.time()
        print('函数运行时间为：%.2fs' % (end_time - start_time))

    return result


@timeit
def func_0():
    time.sleep(2)


func_0()


# 二、 函数带参数
def deco(func):
    def _deco(a, b):
        print("before myfunc() called.")
        ret = func(a, b)
        print("  after myfunc() called. result: %s" % ret)
        return ret

    return _deco


@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b


myfunc(1, 2)
myfunc(3, 4)


# 三、 函数带不定参

def deco(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret

    return _deco


@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b


@deco
def myfunc2(a, b, c):
    print(" myfunc2(%s,%s,%s) called." % (a, b, c))
    return a + b + c


myfunc(1, 2)
myfunc(3, 4)
myfunc2(1, 2, 3)
myfunc2(3, 4, 5)

# 四、 装饰器带参数

from functools import wraps
import logging


def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(level, logmsg)
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

add(2, 4)
spam()


# 五、 让装饰器带 类 参数
class locker:
    def __init__(self):
        print("locker.__init__() should be not called.")

    @staticmethod
    def acquire():
        print("locker.acquire() called.（这是静态方法）")

    @staticmethod
    def release():
        print("  locker.release() called.（不需要对象实例）")


def deco(cls):
    '''cls 必须实现acquire和release静态方法'''

    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()

        return __deco

    return _deco


@deco(locker)
def myfunc():
    print(" myfunc() called.")


myfunc()
