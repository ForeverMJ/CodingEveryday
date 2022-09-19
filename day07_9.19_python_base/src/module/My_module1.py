__all__ = ['fn1','fn2']  # from ... import .. 会限制


def fn1():
    print("我是模块中的fn1函数")

def fn2():
    print("我是模块中的fn2函数")

def fn3():
    print("我是模块中的fn3函数")

def fn4():
    print("我是模块中的fn4函数")

def fn5():
    print("我是模块中的fn5函数")


if '_name_' == '_main_' :
 fn1()