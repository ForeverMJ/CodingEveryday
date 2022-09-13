'''

     格式：
        变量 = 【元素1，元素2，元素3......】


'''

list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
#如何获取列表的数据呢？
print(list1[0:5])#0から　５数字
print(list1[1]) #数组第2个

#遍历操作 for while
for i in list1:
    print(i)

l = len(list1)

print('--------------------')
i = 0
while i < l:
    print(list1[i])
    i += 1
print('-' * 20)

