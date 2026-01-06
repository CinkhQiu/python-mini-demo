# 事件驱动，asyncio，GUI / 网络编程
import time
from datetime import datetime

def timer(seconds, callback):
    print(datetime.now().strftime("%H:%M:%S"))
    time.sleep(seconds)
    callback()

def printTime():
    print(datetime.now().strftime("%H:%M:%S"))

timer(5, printTime)