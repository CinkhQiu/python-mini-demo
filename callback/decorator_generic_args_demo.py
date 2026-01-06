def log_call(func):
    """
    A generic decorator that works with any function signature
    """
    def wrapper(*args, **kwargs):
        print(f"[LOG] calling {func.__name__}")
        print(f"      args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} finished")
        return result
    return wrapper


@log_call
def add(a, b):
    return a + b


@log_call
def greet(name, greeting="hello"):
    print(f"{greeting}, {name}!")


if __name__ == "__main__":
    r = add(2, 3)
    print("result:", r)

    greet("Alice")
    greet("Bob", greeting="hi")