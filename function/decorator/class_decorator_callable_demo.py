"""
本示例用于说明一个统一的语言模型：

装饰器不要求是函数，
只要对象是可调用的（callable），
就可以作为装饰器使用。

该能力基于 Python 的 __call__ 协议。
"""


class SimpleDecorator:
    """
    一个基于类实现的装饰器。

    类实例通过实现 __call__ 方法，
    使自身成为一个可调用对象，
    从而可以接收并替换函数对象。
    """

    def __call__(self, func):
        """
        当类实例作为装饰器使用时，
        该方法在函数定义阶段被调用。

        它接收原函数对象，并返回一个新的函数对象。
        """
        def wrapper(*args, **kwargs):
            print("before call")
            result = func(*args, **kwargs)
            print("after call")
            return result

        return wrapper


@SimpleDecorator()
def greet(name):
    """
    一个简单的示例函数，用于演示类装饰器的工作方式。
    """
    print(f"hello, {name}")


print("calling greet:")
greet("world")