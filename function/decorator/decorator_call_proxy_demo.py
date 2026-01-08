"""
本示例用于说明装饰器中 wrapper 的核心职责：

wrapper 的本质是“调用代理（call proxy）”，
它必须能够透明地接收并转发任意参数，
否则将破坏被装饰函数原有的调用约定。

本示例将展示：
1. 不使用 *args, **kwargs 会导致什么问题
2. 使用 *args, **kwargs 如何保持调用透明性
"""


def bad_decorator(func):
    """
    一个错误示例的装饰器。

    该装饰器返回的 wrapper 没有接收任何参数，
    会直接破坏原函数的参数绑定规则。
    """
    def wrapper():
        print("before call (bad)")
        result = func()
        print("after call (bad)")
        return result

    return wrapper


def good_decorator(func):
    """
    一个正确示例的装饰器。

    wrapper 使用 *args 和 **kwargs 接收任意参数，
    并将其原样转发给被装饰函数，从而保持调用语义不变。
    """
    def wrapper(*args, **kwargs):
        print("before call (good)")
        result = func(*args, **kwargs)
        print("after call (good)")
        return result

    return wrapper


@bad_decorator
def add_bad(a, b):
    """
    一个带有位置参数的示例函数。

    该函数用于演示：
    当 wrapper 不接收参数时，函数调用将直接失败。
    """
    return a + b


@good_decorator
def add_good(a, b):
    """
    一个带有位置参数的示例函数。

    该函数用于演示：
    使用 *args, **kwargs 的 wrapper 可以正确代理调用。
    """
    return a + b


print("calling add_good(1, 2):")
print("result =", add_good(1, 2))

print("\ncalling add_bad(1, 2):")
try:
    print("result =", add_bad(1, 2))
except TypeError as e:
    print("TypeError:", e)