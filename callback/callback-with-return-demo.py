def burger_maker(callback):
    print("🍞 准备面包")
    print("🔥 加热面包")

    # callback returns something
    sauce = callback()

    print(f"🧂 加入酱料：{sauce}")
    print("🧀 加入奶酪片")
    print("🥬 加入蔬菜")
    print("✅ 汉堡制作完成\n")


def beef_sauce():
    print("🥩 处理牛肉")
    print("🥫 调制牛肉专用酱")
    return "黑椒牛肉酱"


def chicken_sauce():
    print("🍗 处理鸡肉")
    print("🥗 调制清爽沙拉酱")
    return "凯撒沙拉酱"


if __name__ == "__main__":
    burger_maker(beef_sauce)
    burger_maker(chicken_sauce)