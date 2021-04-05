# @dese: 这是总结 python 装饰器用法的地方 -- 偏函数 + 类
# @date: 2021/04/05
# @author：小十二


"""
偏函数

1、什么是偏函数
Python 偏函数是通过 functools 模块被用户调用。

它的作用是在函数调用前，预先固定参数的方法。
如果你的函数需要 x 和 y 两个参数，实现把 x 参数固定了，后续调用只需要传入 y 即可，例子：

参考文档：https://n3xtchen.github.io/n3xtchen/python/2015/04/20/python-clean-code-through-partial-function-application
案例1 - 重构特定领域表达式
案例2 - 使用偏函数构建伪对象继承

"""

import functools

def adder(x, y):
    return x + y

# 执行它
assert adder(1, 1) == 2
assert adder(5, 5) == 10
assert adder(6, 2) == 8

# 把 y 的参数固定
add_five = functools.partial(adder, y=5)

# 现在 加上 5
# x =1, y =5
assert add_five(1) == 6
# x =5, y =5
assert add_five(5) == 10
# x =2, y =5
assert add_five(2) == 7



"""
偏函数 + 类 的装饰器


如下所示，DelayFunc 是一个实现了 __call__ 的类，delay 返回一个偏函数，在这里 delay 就可以做为一个装饰器。

"""
import time
import functools


class DelayFunc:
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} seconds...')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print('Call without delay')
        return self.func(*args, **kwargs)


def delay(duration):
    """
    装饰器：推迟某个函数的执行。
    同时提供 .eager_call 方法立即执行
    """
    # 此处为了避免定义额外函数，
    # 直接使用 functools.partial 帮助构造 DelayFunc 实例
    return functools.partial(DelayFunc, duration)

@delay(duration=2)
def add(a, b):
  return a+b

add(3,5)
# >>> add  # 可见 add 变成了 Delay 的实例
# <__main__.DelayFunc object at 0x107bd0be0>
# >>>
# >>> add(3,5) # 直接调用实例，进入 __call__
# Wait for 2 seconds...
# 8
# >>>
# >>> add.func # 实现实例方法
# <function add at 0x107bef1e0>
