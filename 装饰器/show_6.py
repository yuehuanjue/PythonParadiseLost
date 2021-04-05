# @dese: 这是总结 python 装饰器用法的地方 -- 创建装饰器时保留函数元信息
# @date: 2021/04/05
# @author：小十二


"""
保留函数元信息


问题：
    写了一个装饰器作用在某个函数上，但是这个函数的重要的元信息比如名字、文档字符串、注解和参数签名都丢失了。

解决方案：
    使用 functools 库中的 @wraps 装饰器来注解底层包装函数。

示例:

"""

import time
from functools import wraps
def timethis(func):
    """
        Decorator that reports the execution time.
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1

""" 使用了 @wraps(func) 的结果"""
# >>> countdown(100000)
# countdown 0.008917808532714844
# >>> countdown.__name__
# 'countdown'
# >>> countdown.__doc__
# '\n\tCounts down\n\t'
# >>> countdown.__annotations__
# {'n': <class 'int'>}


""" 没使用 @wraps(func) 的结果"""
# >>> countdown.__name__
# 'wrapper'
# >>> countdown.__doc__
# >>> countdown.__annotations__
# {}

"""
@wraps 有一个重要特征是它能让你通过属性 __wrapped__ 直接访问被包装函数。例如:

>>> countdown.__wrapped__(100000)

__wrapped__ 属性还能让被装饰函数正确暴露底层的参数签名信息。例如：

>>> from inspect import signature
>>> print(signature(countdown))
(n:int)

一个很普遍的问题是怎样让装饰器去直接复制原始函数的参数签名信息， 如果想自己手动实现的话需要做大量的工作，
最好就简单的使用 @wraps 装饰器。 通过底层的 __wrapped__ 属性访问到函数签名信息
"""
