"""
iterator_basic_protocol_demo.py

演示内容：
1. 迭代器协议的最小实现
2. __iter__ 与 __next__ 的职责
3. StopIteration 如何终止迭代
"""


class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


if __name__ == "__main__":
    counter = Counter(3)

    for v in counter:
        print(v)