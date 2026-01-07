"""
async_concurrent_tasks_demo.py

演示内容：
1. 多个协程的并发执行
2. asyncio.create_task 的作用
3. await 等待多个任务完成
"""

import asyncio


async def worker(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} finished")


async def main():
    t1 = asyncio.create_task(worker("A", 1))
    t2 = asyncio.create_task(worker("B", 2))
    t3 = asyncio.create_task(worker("C", 1))

    await t1
    await t2
    await t3


if __name__ == "__main__":
    asyncio.run(main())