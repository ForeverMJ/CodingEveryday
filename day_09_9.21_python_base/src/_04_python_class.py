# 演示： python的类中私有属性和私有方法

class Dog():

    def __init__(self):
        self.name = 'king'
        # 私有属性
        self.__age = 5

# 一般提供 getter 和 setter方法
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
       # 私有方法
    def __eat(self):
         print('金毛，喜欢吃狗粮')

# 构建Dog对象
dog = Dog()
# 外界是无法直接访问私有属性和私有方法
print(dog.name)
# # print(dog.age)
#
# dog.eat()

print(dog.get_age())