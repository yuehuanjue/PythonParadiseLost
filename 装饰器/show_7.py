# @dese: 这是总结 python 装饰器用法的地方 -- 解除一个装饰器
# @date: 2021/04/05
# @author：小十二


"""
解除一个装饰器


问题：
    一个装饰器已经作用在一个函数上，你想撤销它，直接访问原始的未包装的那个函数。

解决方案：
    假设装饰器是通过 @wraps 来实现的，那么你可以通过访问 __wrapped__ 属性来访问原始函数

注：
    1、直接访问未包装的原始函数在调试、内省和其他函数操作时是很有用的。
    2、此方案仅仅适用于在装饰器中正确使用了 @wraps 或者直接设置了 __wrapped__ 属性的情况。
    3、如果有多个装饰器，那么访问 __wrapped__ 属性的行为是不可预知的
    4、对于内置的装饰器 @staticmethod 和 @classmethod 就没有遵循这个约定 (它们把原始函数存储在属性 __func__ 中)。

示例:

"""

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper


@decorator
def add(x, y):
    print(x + y)
    return x + y


add(2, 3)  # 使用装饰器
# Decorator 1
# 5
add.__wrapped__(2, 3)  #解除装饰器的使用
# 5
