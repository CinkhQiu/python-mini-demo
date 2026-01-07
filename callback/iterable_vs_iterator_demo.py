"""
iterable_vs_iterator_demo.py

演示内容：
1. 可迭代对象与迭代器的区别
2. __iter__ 返回“新的迭代器”
3. 为什么 list 可以反复 for
"""


class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return RangeIterator(self.start, self.end)


class RangeIterator:
    def __init__(self, current, end):
        self.current = current
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


if __name__ == "__main__":
    r = MyRange(0, 3)

    print("first loop:")
    for v in r:
        print(v)

    print("second loop:")
    for v in r:
        print(v)