# 带有参数的装饰器demo
def repeat(times):
    """
    times: how many times to repeat the function call
    """
    def decorator(func):
        def wrapper():
            for i in range(times):
                print(f"call {i + 1}")
                func()
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print("hi!")


if __name__ == "__main__":
    say_hi()