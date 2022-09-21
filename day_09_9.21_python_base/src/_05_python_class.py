# 演示 python的类的单继承和多继承

class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("只要是动物，需要吃饭")

    def sleep(self):
        print("只要是动物，需要睡觉")
# 一旦选择了继承，子类可以继承父类中的方法和属性
class Dog(Animal):
    # 重写父类属性
    def __init__(self,age,address):
        super(Dog, self).__init__('阿毛',age)

        self.address = address


    # 重写父类的方法：
    def eat(self):
        # 是否可以调用父类的方法呢？ super()
        super().eat()
        print('狗爱吃骨肉')

# 构建子类
dog = Dog(5, '广州')



dog.eat()
dog.sleep()
print(dog.name)
print(dog.age)
print(dog.address)

