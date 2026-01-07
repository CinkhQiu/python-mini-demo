"""
generator_yield_from_demo.py

演示内容：
1. yield from 的基本语义
2. 子生成器与父生成器的组合
3. yield from 等价于“手写 for + yield”
"""


def sub_generator():
    yield 1
    yield 2
    yield 3


def parent_generator_manual():
    for x in sub_generator():
        yield x


def parent_generator_yield_from():
    yield from sub_generator()


if __name__ == "__main__":
    print("=== manual composition ===")
    for v in parent_generator_manual():
        print(v)

    print("\n=== yield from composition ===")
    for v in parent_generator_yield_from():
        print(v)