# @dese: 这是总结 python 装饰器用法的地方 -- 将装饰器定义为类的一部分
# @date: 2021/04/05
# @author：小十二


"""
将装饰器定义为类的一部分


问题：
    在类中定义装饰器，并将其作用在其他函数或方法上


示例:

"""
from functools import wraps


class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)

        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)

        return wrapper


a = A()


@a.decorator1  # 实例调用
def spam():
    print("====== spam =======")


# As a class method
@A.decorator2  # 类调用
def grok():
    print("====== grok =======")

spam()
grok()

"""
@property 装饰器实际上是一个类，它里面定义了三个方法 getter(), setter(), deleter() , 每一个方法都是一个装饰器。
如：
"""
# Create a property instance
first_name = property()

class Person:
    # Create a property instance
    first_name = property()

    # Apply decorator methods
    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value
