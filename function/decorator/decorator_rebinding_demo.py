"""
本示例用于说明 Python 装饰器的本质：

装饰器不是“给函数增加功能”，
而是在函数定义阶段，将原函数对象
重绑定（rebinding）为另一个可调用对象。

也就是说：

@decorator
def f():
    ...

在语义上等价于：

def f():
    ...

f = decorator(f)
"""


def decorator(func):
    """
    装饰器函数，用于接收一个函数对象，并返回一个新的函数对象。

    该函数在“函数定义完成后、函数调用之前”执行。
    它的返回值将会替换原本的函数名绑定。
    """
    print("decorator 被调用，接收到的 func =", func)

    def wrapper():
        """
        包装函数，用于替代原函数。

        实际被调用的是这个函数，而不是原始的 func。
        原函数仅作为一个被保存的变量存在于闭包中。
        """
        print("wrapper 被调用（调用前）")
        func()
        print("wrapper 被调用（调用后）")

    return wrapper


print("函数定义之前")


@decorator
def f():
    """
    原始函数定义。

    注意：该函数体本身并不会直接与名字 f 绑定，
    f 最终绑定的是 decorator 返回的 wrapper。
    """
    print("原始函数 f 的函数体执行")


print("函数定义之后")

print("\n装饰完成后，查看 f 的真实信息：")
print("f =", f)
print("f.__name__ =", f.__name__)
print("id(f) =", id(f))

print("\n调用 f()：")
f()