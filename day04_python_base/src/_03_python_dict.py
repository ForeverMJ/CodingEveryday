# dirc类似java中的map

# 演示字典相关操作

'''
    格式：
         变量 = {'key1':'value1,'key2':'value2'....}

'''

stu = {'name': 'james', 'age': 18, 'address': 'beijing'}

# 获取数据
print(stu['name'])
# print(stu['sex'])  # 当获取一个不存在的key的时候，会直接报错

print(stu.get('age'))
print(stu.get('sex','man'))  # 当不存在的时候，返回none,'man'也支持设置默认值

# 修改元素
stu['name'] = '李四'
print(stu)

# 添加元素
stu['sex'] = 'fmale'
print(stu)

# 删除元素

del stu['name']
print(stu)

# del stu  # 将整个stu删除

# stu.clear()  # 清空操作

# print(stu)

print(stu.items())    # 显示所有的键值对




