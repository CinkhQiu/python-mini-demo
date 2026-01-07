"""
compare_asyncio_demo.py

演示内容：
1. asyncio 并发执行多个协程
2. await 在 I/O 等待时让出控制权
3. 单线程完成并发任务
"""

import asyncio
import time


async def task(name):
    await asyncio.sleep(2)
    print(f"{name} done")


async def main():
    tasks = [asyncio.create_task(task(f"task-{i}")) for i in range(3)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print("elapsed:", time.time() - start)