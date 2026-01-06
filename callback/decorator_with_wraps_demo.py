"""
decorator_with_wraps_demo.py

演示内容：
1. functools.wraps 的作用
2. 如何保留被装饰函数的元信息
3. 为什么在真实项目中必须使用 wraps
functools.wraps 的本质：
1.让 wrapper “伪装”成原函数，而不是取代它
"""

from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} finished")
        return result
    return wrapper

def log_call_without_wraps(func):
    def wrapper(*args, **kwargs):
        """
        func = wrapper
        此时的func指向wrapper
        """
        print(f"[LOG] calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} finished")
        return result
    return wrapper


@log_call
def add(a, b):
    """Add two numbers"""
    return a + b

@log_call_without_wraps
def sub(a, b):
    """Sub two numbers"""
    return a - b


if __name__ == "__main__":
    print("result:", add(2, 3))
    print("function name:", add.__name__)
    print("docstring:", add.__doc__)
    print("------------------------------")
    print("result:", sub(2, 3))
    print("function name:", sub.__name__)
    print("docstring:", sub.__doc__)
