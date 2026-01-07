"""
async_io_sleep_demo.py

演示内容：
1. 使用 asyncio.sleep 模拟 I/O 操作
2. 多个 I/O 任务的并发执行
3. async 并发在 I/O 场景下的价值
"""

import asyncio


async def fetch(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} done")


async def main():
    tasks = [
        asyncio.create_task(fetch("task-1", 2)),
        asyncio.create_task(fetch("task-2", 1)),
        asyncio.create_task(fetch("task-3", 3)),
    ]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())