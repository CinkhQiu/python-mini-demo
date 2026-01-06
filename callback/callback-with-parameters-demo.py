def burgerMaker(callback):
    print("把面包加热至金黄色")
    callback("双层")
    print("加入奶酪片")
    print("将食材组装在一起")

def beefBurger(style):
    print(f"加热{style}牛肉片")
    print("牛肉片刷上汉堡酱")

burgerMaker(beefBurger)
print("****双层牛肉汉堡完成啦!****")
burgerMaker(lambda style: print(f"加入{style}鸡肉饼"))
print("****双层鸡肉汉堡完成啦!****")