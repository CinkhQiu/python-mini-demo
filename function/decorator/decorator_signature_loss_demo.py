"""
本示例用于说明一个核心事实：

装饰器如果不使用 functools.wraps，
将会导致被装饰函数的元信息（如 __name__、__doc__、signature）
被 wrapper 覆盖，从而破坏 Python 的自省（introspection）能力。

该问题在框架（如 Flask / FastAPI）中尤为致命。
"""

import inspect
from functools import wraps


def decorator_without_wraps(func):
    """
    一个未使用 functools.wraps 的装饰器。

    该装饰器会返回 wrapper，
    但不会保留原函数的任何元信息。
    """
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def decorator_with_wraps(func):
    """
    一个正确使用 functools.wraps 的装饰器。

    wraps 会将原函数的元信息复制到 wrapper 上，
    从而保持函数在 introspection 层面的透明性。
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@decorator_without_wraps
def func_without_wraps(a: int, b: int) -> int:
    """
    示例函数：未使用 wraps 的装饰结果。
    """
    return a + b


@decorator_with_wraps
def func_with_wraps(a: int, b: int) -> int:
    """
    示例函数：使用 wraps 的装饰结果。
    """
    return a + b


print("=== without wraps ===")
print("name:", func_without_wraps.__name__)
print("doc :", func_without_wraps.__doc__)
print("signature:", inspect.signature(func_without_wraps))

print("\n=== with wraps ===")
print("name:", func_with_wraps.__name__)
print("doc :", func_with_wraps.__doc__)
print("signature:", inspect.signature(func_with_wraps))