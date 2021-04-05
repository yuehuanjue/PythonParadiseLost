# @dese: 这是总结 python 装饰器用法的地方 -- 类装饰器
# @date: 2021/04/05
# @author：小十二


"""
一、 不带参数的类装饰器

基于类装饰器的实现，必须实现 __call__ 和 __init__两个内置函数。

__init__ ：接收被装饰函数
__call__ ：实现装饰逻辑。
"""


class logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[INFO]: the function {func}() is running..." \
              .format(func=self.func.__name__))
        return self.func(*args, **kwargs)


@logger
def say(something):
    print("say {}!".format(something))


say("hello")

"""
二、 带参数的类装饰器

带参数和不带参数的类装饰器有很大的不同。

__init__ ：不再接收被装饰函数，而是接收传入参数。
__call__ ：接收被装饰函数，实现装饰逻辑。
"""


class logger(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):  # 接受函数
        def wrapper(*args, **kwargs):
            print("[{level}]: the function {func}() is running..." \
                  .format(level=self.level, func=func.__name__))
            func(*args, **kwargs)

        return wrapper  # 返回函数


@logger(level='WARNING')
def say(something):
    print("say {}!".format(something))


say("hello")
