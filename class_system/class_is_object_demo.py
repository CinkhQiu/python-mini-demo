"""
class_is_object_demo.py

目的：
演示「类本身也是对象」在 Python 中到底意味着什么，
以及“没有实例化的类”到底有什么用。

核心对照：
- C++：class 只是类型说明
- Python：class 是一个运行期对象
"""

# ----------------------------
# 1. 定义一个类（此时还没有任何实例）
# ----------------------------

class User:
    version: float
    def greet(self):
        print("hello")


print("=== 基本事实 ===")
print("User:", User)
print("type(User):", type(User))
print("isinstance(User, object):", isinstance(User, object))
print()

# ----------------------------
# 2. 类可以像普通对象一样被传参
# ----------------------------

def receive_class(cls):
    print("receive_class got:", cls)

receive_class(User)
print()

# ----------------------------
# 3. 类可以被赋值、放进容器
# ----------------------------

A = User
classes = [User, int, str]

print("A is User:", A is User)
print("classes:", classes)
print()

# ----------------------------
# 4. 类可以在运行期被“修改”
# ----------------------------

User.version = 1.0

print("User.version:", User.version)
print()

# ----------------------------
# 5. 类可以在运行期被调用（生成实例）
# ----------------------------

u = User()
print("u:", u)
print("type(u):", type(u))
print()

# ----------------------------
# 6. 类 ≈ type(...) 的返回值
# ----------------------------

DynamicUser = type(
    "DynamicUser",
    (),
    {
        "greet": lambda self: print("hello from DynamicUser")
    }
)

print("DynamicUser:", DynamicUser)
print("type(DynamicUser):", type(DynamicUser))

du = DynamicUser()
du.greet()