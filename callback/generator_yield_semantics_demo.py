"""
generator_yield_semantics_demo.py

演示内容：
1. 什么是生成器函数
2. yield 如何“暂停并恢复”函数执行
3. next() 如何驱动生成器向前运行
4. for 循环是如何使用生成器的
"""


def simple_generator():
    print("step 1")
    yield 1

    print("step 2")
    yield 2

    print("step 3")
    yield 3

    print("generator finished")


def manual_drive():
    """
    演示：使用 next() 手动驱动生成器
    """
    g = simple_generator()

    print("call next()")
    print(next(g))

    print("call next()")
    print(next(g))

    print("call next()")
    print(next(g))

    try:
        print("call next() again")
        next(g)
    except StopIteration:
        print("StopIteration raised")


def for_loop_drive():
    """
    演示：for 循环如何自动驱动生成器
    """
    for value in simple_generator():
        print("got:", value)


if __name__ == "__main__":
    print("=== manual drive ===")
    manual_drive()

    print("\n=== for loop drive ===")
    for_loop_drive()