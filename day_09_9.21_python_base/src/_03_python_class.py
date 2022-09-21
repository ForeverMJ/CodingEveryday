# 演示 python的类中魔术方法

#  __init__

class Student():
    # 当实例化对象的时候, __init__ 方法就会被触发执行, 从而构建Stu对象
    def __init__(self, name=None, sex=None, age=None):
        self.name = name
        self.sex = sex
        self.age = age

    # 类似于java中toString()
    # TypeError: __str__ returned non-string (type NoneType)  在使用 __str__ 要求return返回结果
    def __str__(self):
        return f'{self.name},{self.sex},{self.age}'

    # 当执行对象被删除的时候, python解析器会调用del() 方法
    def __del__(self):
        print(f"{self} 对象以及被删除了")


    def eat(self):
        print("人人都是要吃饭滴....")

    def study(self):
        print("人人都应该学习")





# 创建对象
stu = Student('李四', '男', 35)

stu.eat()
print(stu.name)
print(stu.sex)
print(stu.age)

print(stu)
