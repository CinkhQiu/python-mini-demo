"""
async_basic_await_demo.py

演示内容：
1. async 函数与 await 的最小用法
2. await 如何“让出控制权”
3. asyncio.run 的作用
"""

import asyncio


async def task():
    await asyncio.sleep(1)
    print("task done")


async def main():
    print("start")
    await task()
    print("end")


if __name__ == "__main__":
    asyncio.run(main())