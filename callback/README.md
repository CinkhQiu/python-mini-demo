# Python Control Flow & Concurrency Mini Demos

本目录用于系统性练习 Python 中 **控制流抽象与并发模型**，  
所有示例均为「最小可运行 demo」，按**思想主线**而非语法碎片组织。

学习与复盘建议：**从上到下顺序阅读与运行**。

---

## 一、Callback（函数作为控制单元）

> 核心主题：把“做什么 / 何时做”交出去

### 基础回调
- `callback-demo.py`
- `callback-with-parameters-demo.py`
- `callback-with-return-demo.py`

### 回调的实际应用
- `callback-sort-by-key.py` —— key 函数（投影而非比较）
- `callback-timer.py` —— 定时回调
- `callback-hook.py` —— hook / error callback

### 回调 + 装饰器雏形
- `callback-decorator.py`

---

## 二、Decorator（函数调用方式的控制）

> 核心主题：在不改业务代码的情况下，插入横切逻辑

### 装饰器基础
- `decorator_with_args_demo.py`
- `decorator_generic_args_demo.py`

### 装饰器工程化
- `decorator_with_wraps_demo.py` —— 保留函数元信息（functools.wraps）

---

## 三、Context Manager（with 语句）

> 核心主题：控制“进入 / 退出”时机（资源生命周期）

### class 版上下文管理器
- `context_manager_basic_demo.py`

### generator 版上下文管理器
- `context_manager_generator_demo.py`

---

## 四、Generator（yield 与惰性执行）

> 核心主题：可暂停函数 + 惰性计算

### yield 基础语义
- `generator_yield_semantics_demo.py`

### 生成器组合
- `generator_yield_from_demo.py`

### 生成器流水线（真实使用场景）
- `generator_pipeline_demo.py`

---

## 五、Iterator Protocol（生成器的底层）

> 核心主题：for 循环真正依赖的协议

### 迭代器最小实现
- `iterator_basic_protocol_demo.py`

### iterable vs iterator 区分
- `iterable_vs_iterator_demo.py`

---

## 六、Async / Await（协程与事件循环）

> 核心主题：单线程并发，I/O 友好

### async / await 基础
- `async_basic_await_demo.py`
- `async_concurrent_tasks_demo.py`

### async + I/O 场景
- `async_io_sleep_demo.py` —— 模拟 I/O
- `async_file_io_demo.py` —— 阻塞 I/O 的现实处理方式

---

## 七、Concurrency Model Comparison（并发模型对比）

> 同一任务，不同模型，对比直觉差异

- `compare_threading_demo.py`
- `compare_asyncio_demo.py`
- `compare_multiprocessing_demo.py`

---

## 推荐复盘顺序（最重要）