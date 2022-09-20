# 演示 python的装饰器的实现操作
# 装饰器：  主要是用于对已有函数进行增强，而且不改变原有函数代码 也不改变原有调用方案
# 装饰器： 参数必须有且只能有一个参数，而且这个参数必须是一个函数
def de_fn(p):
    def deco_fn(fn):
        def zq_inn(num1, num2):
            if p == '+':
                print("执行 加法操作")
            elif p == '-':
                print("执行 减法操作")

                res = fn(num1, num2)
                return res

        return zq_inn

    return deco_fn


@de_fn('+')
def add(a, b):
    res = a + b
    return res


# add = deco_fn(add, '-')

res = add(5, 10)
print(res)
