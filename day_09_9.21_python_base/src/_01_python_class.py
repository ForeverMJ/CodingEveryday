# 演示类的一些相关操作
'''
 格式：
     class 类名：
          代码。。。
     或者
     class 类名（）：
          代码...
'''

# 定义类
class Student():
     # self 是类中的一个特殊关键词，用于指向这个类的实例化本身，类似于java中的this
    def eat(self):
        print(self)
        print("人人都要吃饭...")
    def study(self):
        print("人人都应该学习")

# 如何实例化这个类呢？ 如何创建对象
# 格式： 对象名 = 类名（）

# 创建对象
stu = Student()

print(stu)  # 默认打印对象的地址
stu.eat()
stu.study()