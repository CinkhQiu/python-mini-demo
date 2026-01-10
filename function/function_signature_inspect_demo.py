"""
function_signature_inspect_demo.py

演示内容：
1. 使用 inspect.signature 在运行期读取函数签名
2. 参数对象 Parameter 的结构与属性
3. Python 如何区分不同类型的参数
4. 函数签名作为“运行期数据结构”的意义

目标：
理解 Python 框架是如何在运行时“理解并操作函数接口”的
"""

import inspect

def example_func(a, b: int, /, c=3, *, d, e=5, **kwargs):
    """
    示例函数，用于展示完整的函数签名结构。

    参数说明：
    - a, b：仅位置参数
    - c：位置或关键字参数，带默认值
    - d：关键字专用参数，必须提供
    - e：关键字专用参数，带默认值
    - **kwargs：接收额外关键字参数

    返回值：
    无实际返回，仅用于签名分析
    """
    pass


def inspect_function_signature(func):
    """
    函数 = 可调用对象 + 一堆元数据

    打印指定函数的签名信息与各参数的详细属性。

    参数：
    - func：任意 Python 函数对象

    行为：
    - 输出函数签名字符串
    - 逐个输出参数的名称、类型与默认值信息
    """
    sig = inspect.signature(func)
    print("signature:", sig)

    for name, param in sig.parameters.items():
        print(
            f"name={name}, "
            f"kind={param.kind}, "
            f"default={param.default}, "
            f"annotation={param.annotation}"
        )


def is_required_parameter(param):
    """
    判断一个参数在调用时是否为必需参数。

    参数：
    - param：inspect.Parameter 对象

    返回值：
    - True：参数必须由调用方提供
    - False：参数有默认值或可变参数
    """
    return (
        param.default is inspect.Parameter.empty
        and param.kind not in (
            inspect.Parameter.VAR_POSITIONAL,
            inspect.Parameter.VAR_KEYWORD,
        )
    )


def analyze_required_parameters(func):
    """
    分析函数中哪些参数是调用时必须提供的。

    参数：
    - func：任意 Python 函数对象

    行为：
    - 打印所有“必需参数”的名称
    """
    sig = inspect.signature(func)
    required = [
        name
        for name, param in sig.parameters.items()
        if is_required_parameter(param)
    ]
    print("required parameters:", required)


if __name__ == "__main__":
    print("=== inspect signature ===")
    inspect_function_signature(example_func)

    print("\n=== analyze required parameters ===")
    analyze_required_parameters(example_func)