"""
generator_pipeline_demo.py

演示内容：
1. 使用生成器构建数据处理流水线
2. 惰性计算的执行顺序
3. 每个生成器只关注一个处理步骤
"""


def source():
    for i in range(5):
        yield i


def square(numbers):
    for n in numbers:
        yield n * n


def even_filter(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n


if __name__ == "__main__":
    pipeline = even_filter(square(source()))

    for value in pipeline:
        print(value)