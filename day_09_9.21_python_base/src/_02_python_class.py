# 演示类的相关操作
'''
 如何添加属性：
     格式：  对象名.属性名 = 值

'''

class Person():
    def person_info_print(self):
        print(f'姓名：{self.name}')
        print(f'sex:{self.sex}')
        print(f'年龄：{self.age}')

# 创建对象
person = Person()

person.name = '张三'
person.sex = '女'
person.age = '20'

person.person_info_print()
