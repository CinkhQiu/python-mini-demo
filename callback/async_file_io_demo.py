"""
async_file_io_demo.py

演示内容：
1. async 中如何处理阻塞型文件 I/O
2. asyncio.to_thread 的基本用法
3. async 与线程协作的真实写法
"""

import asyncio


def read_file(path):
    with open(path, "r") as f:
        return f.read()


async def main():
    result = await asyncio.to_thread(read_file, "test.txt")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())