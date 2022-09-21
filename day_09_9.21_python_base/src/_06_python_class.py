# 演示: 多态的表示

class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def eat(self):
        print("只要是动物, 就得吃饭")

    def sleep(self):
        print("只要是动物, 就得休息")

# 一旦选择了继承, 子类可以继承父类中方法和属性
class Dog(Animal):

    def __init__(self,age,address):
        # self.name = '阿狗'
        # self.age = age
        super().__init__('阿狗',age)

        self.address = address


    # 重写父类的方法
    def eat(self):
        print("狗爱吃骨头")


class Cat(Animal):

    def eat(self):
        print("猫吃猫粮")


# 采用多态的方式来构建对象
animal1:Animal = Dog(5,'广州')

animal2:Animal = Cat('阿猫',6)


animal1.eat()
animal2.eat()

# 感受多态

def fn1(animal:Animal):
    print(animal)


fn1(Dog(5,'广州'))
fn1(Cat('阿猫',6))