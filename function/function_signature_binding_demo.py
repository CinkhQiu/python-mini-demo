"""
function_signature_binding_demo.py

演示内容：
1. Python 函数参数的绑定规则
2. 位置参数与关键字参数的匹配过程
3. 默认参数的绑定时机
4. *args / **kwargs 在参数绑定中的角色
5. 参数顺序规则对函数签名的影响
6. '/'之前，（positional-only） 强制参数只能按位置传递，防止调用者依赖参数名。
7. '*'之后，（keyword-only）强制参数必须用关键字传递，提高 API 可读性与稳定性。

目标：
理解“函数调用时，Python 如何把实参绑定到形参”
"""

"""
Python 的函数参数传递，本质是：
把“形参名字”绑定到“实参所指向的对象”。
函数内部是否影响外部，只取决于：
1. 是否发生了名字重新绑定
2. 对象是否支持原地修改

Python 里从来不存在“通过形参修改实参变量”这件事，只有“通过共享对象修改对象本身”。
"""


def f1(a, b, c=3):
    print(a, b, c)


def f2(a, b=2, *args):
    print(a, b, args)


def f3(a, *, b, c):
    print(a, b, c)


def f4(a, /, b, c):
    """
    按位置传 = 实参只按出现顺序依次绑定到形参，
    不接受任何关键字指定，
    即使关键字名称和顺序完全正确，也会报错。
    """
    print(a, b, c)


def f5(*args, **kwargs):
    """
    参数规则说明：

    1. *args
       - 用于接收多余的位置参数
       - *args 之后定义的参数，必须以关键字形式传入
       - *args 本身只能按位置传参，不接受关键字绑定

    2. **kwargs
       - 用于接收多余的关键字参数
       - **kwargs 必须位于形参列表的最后
       - **kwargs 之后不能再定义任何参数

    3. 参数顺序约束（从左到右）：
       位置参数 → *args → 关键字专用参数 → **kwargs

    4. *args 与 **kwargs 不参与具体参数绑定，
       它们只负责收集未被其他形参匹配的实参
    """
    print(args, kwargs)


def default_param_demo(x, cache=[]):
    cache.append(x)
    print(cache)


print(f4.__doc__)


if __name__ == "__main__":
    print("=== f1: position + default ===")
    f1(1, 2)
    f1(1, 2, 4)

    print("\n=== f2: *args collection ===")
    f2(1)
    f2(1, 2, 3, 4)

    print("\n=== f3: keyword-only ===")
    f3(1, b=2, c=3)

    print("\n=== f4: positional-only ===")
    f4(1, 2, 3)

    print("\n=== f5: args + kwargs ===")
    f5(1, 2, x=3, y=4)

    print("\n=== default parameter binding ===")
    default_param_demo(1)
    default_param_demo(2)
