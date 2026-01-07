"""
compare_multiprocessing_demo.py

演示内容：
1. multiprocessing 的基本使用
2. 多进程实现真正的并行
3. 每个进程有独立的 Python 解释器
"""

import multiprocessing
import time


def task(name):
    time.sleep(2)
    print(f"{name} done")


if __name__ == "__main__":
    start = time.time()

    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=task, args=(f"task-{i}",))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("elapsed:", time.time() - start)