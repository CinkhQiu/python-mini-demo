# 装饰器 = callback 的语法糖
def simple_decorator(func):
    """
    func: the original function being decorated
    """
    def wrapper():
        print("before function call")
        func()
        print("after function call")
    return wrapper


@simple_decorator
def say_hello():
    print("hello!")

@simple_decorator
def say_byebye():
    print("Bye bye!")


if __name__ == "__main__":
    say_hello()
    say_byebye()