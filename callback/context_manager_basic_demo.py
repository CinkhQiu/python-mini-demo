"""
context_manager_basic_demo.py

演示内容：
1. with 语句的基本用法
2. 上下文管理器的核心协议：__enter__ / __exit__
3. with 如何保证“进入-退出”成对执行
"""


class DemoContext:
    def __enter__(self):
        print("enter context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit context")
        return False


def normal_flow():
    """
    演示：with 语句在正常执行路径下的行为
    """
    with DemoContext():
        print("doing work")


def exception_flow():
    """
    演示：with 语句在发生异常时依然会执行退出逻辑
    """
    try:
        with DemoContext():
            print("doing work")
            raise ValueError("something wrong")
    except ValueError:
        print("exception caught")


if __name__ == "__main__":
    print("=== normal flow ===")
    normal_flow()

    print("\n=== exception flow ===")
    exception_flow()