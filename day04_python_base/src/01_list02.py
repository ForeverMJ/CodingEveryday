# 9.16日coding
# 3 - 查询元素 in     not in
# 需求：  查询F是否在元素中 列表中数据类型都是一样的
list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
flag = 'F' in list1    # F是否在列表中
print(flag)

if 'F' in list1:
    print("存在的")

# flag = 'G' not in list1 #G是否不在列表中
# print(flag)

print(list1.index('F'))     # 直接报出索引位置
# print(list1.index('F', 2 ,5))   # 当索引不到的时候，直接报错

print(list1.count('E'))    # 统计 元素在列表出现了多少次
print(list1)

# 4- 删除元素 del pop
del list1[1]     # 可以用于删除指定位置的元素

print(list1)

print(list1.pop())     # 用于从后弹出一个元素，并将这个元素返回来

print(list1)

list1.remove('E')      # 删除指定的元素
print(list1)

# 5- 排序
list3 = [1, 5, 7, 4, 2, 3, 9, 7, 8]
list3.reverse()
print(list3)
list3.sort()       # sort默认 升序排序

print(list3)

list3.sort(reverse=True)     # 反向排序
print(list3)

list3.reverse()
print(list3)

# 列表 嵌套使用，类似于二维数组

city_list = [['广州', '深圳', '东湾'], ['北京', '天津', '重庆'], ['青岛', '烟台', '威海']]

print(city_list[0][1])

# 列表 支持推导式写法
print('-'*20)
# 需求 生成一个 1-10 的列表数据

list4 = []

for i in range(10):
    list4.append(i+1)
print(list4)

# 推导式写法:
list4 = [i+1 for i in range(10)]

print(list4)

# 带有IF判断的推导式
# 需求 获取1-10之间的偶数
list4 = [i+1 for i in range(10) if (i+1) % 2 == 0]
print(list4)

# 带有多个for循环操作  采用一行代码来实现循环操作
list4 = [(i, j) for i in range(2, 5) for j in range(3)]
print(list4)
