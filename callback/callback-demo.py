def burgerMaker(callback):
    print("把面包加热至金黄色")
    callback()
    print("加入奶酪片")
    print("清洗番茄并切片")
    print("将食材组装在一起")

def beefBurger():
    print("加热牛肉片")
    print("牛肉片刷上汉堡酱")

def chickenBurger():
    print("加入鸡肉饼")
    print("加入沙拉酱")


burgerMaker(beefBurger)
print("****牛肉汉堡已经制作完！****")
burgerMaker(chickenBurger)
print("****鸡肉汉堡已经制作完！****")