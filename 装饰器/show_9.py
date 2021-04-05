# @dese: 这是总结 python 装饰器用法的地方 -- 可选参数的装饰器
# @date: 2021/04/05
# @author：小十二


"""
可选参数的装饰器


问题：
    写了一个装饰器，可以给它参数，也可以不给的方式。

示例:

"""
import logging
from functools import wraps, partial


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


# Example use
@logged
def add(x, y):
    print(x + y)


@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')


add(6, 8)
spam()