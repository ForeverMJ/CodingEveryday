# 演示 python的函数

'''
    定义python的函数格式
      def 函数名（参数列表）：
          函数体。。。。

    调用函数：
         函数名（参数）


'''


# 定义一个简单的函数，在函数中打印一些相关内容
def print_fun():
    print('itcate')
    print('itheima')


# 调用函数： 必须先定义才能使用

print_fun()


# python对数据类型不约束
# 演示： 向函数传入一些相关的参数，比如如何实现一个 相加操作
def sum_fun(a: int, b: int) -> None:
    res = a + b
    print(res)
    print(a)
    print(b)


    sum_fun(1, 3)

# 演示：  拥有返回值的函数
def sum_fum(a, b):
    return  a + b

    # 调用函数
res = sum_fum(30, 50)

print(res)

# 演示 函数的嵌套使用操作
def sum1(a,b):
    return a+b

def sum2():
    print("这是sum2函数")
    res = sum1(10, 30)
    print(f"结果为{res}")

# 调用
sum2()

# 在函数中 全局变量 和 局部变量
# 局部变量：
def fun_1():
    # 此时a就是局部变量，写在函数里面的
    a = 200
    print(a)

fun_1()

#全局变量
b = 50

def fun_A():
    print(b)
def fun_B():
    # global b   # 定义b为全局变量
    b = 30         # 这个变量是局部变量
    print(b)
fun_A()
fun_B()

print(f"全局变量b：{b}")     # 全局变量 还是50

# 如何通过函数， 一次性返回多个结果
def re_fun1():
    return (1, 2)

print(re_fun1())

# 可以简写
def re_fun2():
    return 1, 2
print(re_fun2())

# 返回值支持拆箱操作
a, b = re_fun2()
print(a)
print(b)

print('-' * 50)
# 演示函数的多种参数 定义参数 和 传递参数

# 1- 位置参数： 在调用函数的时候，根据函数的顺序依次传递对应的函数
def stu_fun(name,sex,address):
    print(f'{name},{sex},{address}')
# 调用函数
stu_fun('张三', '男', '北京')

# 2- 关键字参数： 在传递的时候可以超过指定参数名来传递，对传递顺序没有要求
stu_fun(name='李四',sex='男',address='北京')
stu_fun(sex='男',name='李四',address='北京')
stu_fun('王府',sex='男',address='北京')  # 位置参数必须放在最# 前
# 面

# 3- 缺省参数 ：默认值可以不传递
def stu_fun(name,sex,address='北京'):
    print(f'{name},{sex},{address}')
stu_fun(name='赵六',sex='男')
stu_fun(name='赵六',sex='男',address='广州')

# 4- 不定长参数（可变参数） 在调用函数的时候，可以给函数传递任意个参数
def stu_fun(*args):
    print(args) # 将接受到的数据，默认会转换为一个元组
    print(args[0])
stu_fun('张三','男','北京','2020-10-10')

def stu_fun(**kvargs):    # 默认将其转换为一个字典
    print(kvargs)

stu_fun(name='张三',sex='男',address='北京',date='2020-10-10')

# 交换变量
a = 100
b = 50

c = a
a = b
b = c
print(f'{a},{b}')

# python 简单处理
a,b =b,a
print(f'{a},{b}')

# 如何验证数据类型是可变的，还是不可变的
'''
可变类型：
    列表
    字典
    集合
不可变类型：
   整形
   浮点型
   字符串
   元组

id（变量）获取变量的引用地址）——内存地址


'''
# 验证不可变
a = 10
b = a

print(id(a)) # 4498533344
print(id(b)) # 4498533344

a = 20
print(id(b)) # 4498533344
print(id(a)) # 4365036832

# 验证可变
list1 = [20, 50]
list2 = list1

print(id(list1))   # 140296277545728
print(id(list2))   # 14029627754572

list1.append(80)
print(list2)
print(id(list2))    # 14029627754572
print(id(list1))   # 14029627754572


# 匿名函数
'''
  格式：
      lambda 参数列表： 表达式
      
  注意：
     1- 参数列表 可有可无，函数的中参数 在lambda表达式中完全适用
     2- lambda表达式能接收任何数量的参数，但是只能返回一个表达式的值，表达值只能写成一行
     
     如果表达式代码是多行，必须使用普通函数，不能使用匿名函数
     
     一般当函数只有一行语句的时候，都可以改造为匿名函数
     


'''

def fun_1():
    return '张三'

print(fun_1())

# lambda表达式改写
fun_2 = lambda  : '张三'

print(fun_2())
print(fun_2)

# lambda改写
fun = lambda a,b : a + b

print(fun(1,2))

# 后续应用方向： 将匿名函数作为另一个函数参数，传递到函数中去

def function_(fn):
    a = 10
    b = 20

    res = fn(a,b)

    print(f"结果为：{res}")

# 对 a 和 b进行计算操作
function_(lambda a, b: a + b)
function_(lambda a, b: a - b)
function_(lambda a, b: a * b)
function_(lambda a, b: a / b)

# 我们在调用函数的时候，传递匿名函数，相当于计算的规则，对参数进行操作
#在后续spark中，spark提供非常多的一些支持传递参数的API，使用这些API传递相应规则来完成计算
# 这种使用方案 一般成为 函数式编程


