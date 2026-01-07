"""
compare_threading_demo.py

演示内容：
1. threading 的基本使用
2. 多线程在 I/O 场景下的并发效果
3. 主线程等待所有子线程完成
"""

import threading
import time


def task(name):
    time.sleep(2)
    print(f"{name} done")


if __name__ == "__main__":
    start = time.time()

    threads = []
    for i in range(3):
        t = threading.Thread(target=task, args=(f"task-{i}",))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("elapsed:", time.time() - start)