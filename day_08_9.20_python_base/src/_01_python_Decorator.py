# 演示 python的装饰器的实现操作
# 装饰器： 只要是用于对已有函数进行增强，而不改变原有函数代码，也不改变原有调用方案

# 需求： 对以下函数进行增强，在添加商品之前，需要判断是否已经登陆

def check(fn):
    def logger():
        print("请先登入....")
        fn()

    return logger



def addshop():
    print("添加商品...")




# 开启执行增强操作
addshop = check(addshop)   # 核心包装工程

addshop()

