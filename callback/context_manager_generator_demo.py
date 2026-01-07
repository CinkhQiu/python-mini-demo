"""
context_manager_generator_demo.py

演示内容：
1. 使用 contextlib.contextmanager 定义上下文管理器
2. 生成器版 with 的基本结构
3. yield 前后分别对应 enter / exit 阶段
"""

from contextlib import contextmanager


@contextmanager
def demo_context():
    print("enter context")
    try:
        yield
    finally:
        print("exit context")


def normal_flow():
    """
    演示：生成器版上下文管理器的正常执行流程
    """
    with demo_context():
        print("doing work")


def exception_flow():
    """
    演示：生成器版上下文管理器在异常情况下的行为
    """
    try:
        with demo_context():
            print("doing work")
            raise RuntimeError("something wrong")
    except RuntimeError:
        print("exception caught")


if __name__ == "__main__":
    print("=== normal flow ===")
    normal_flow()

    print("\n=== exception flow ===")
    exception_flow()