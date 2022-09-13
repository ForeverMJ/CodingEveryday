'''
格式：
    while 条件：
      当条件满足时，执行的语句
'''

#需求，打印5次
import time

i = 1
while i <= 5:
    print("hello")
    i += 1   #python中没有i++

#死循环
# while True:
#     print("world")
#     time.sleep(1)
#需求 打印从 1-100之间所有的偶数
i = 1

while i <=100:
    if i % 2 == 0:
        print(i)

    i += 1

#需求： 打印三行三列的*
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print('*', end=' ')
        j += 1

    print() #换行操作
    i += 1
#需求： 打印三行数据，第一行为一个*，第二行 2个*，第三行 3个*
i = 1
while i <= 3:
    j = 1
    while j <= i:
        print('*', end=' ')
        j += 1

    print() #换行操作
    i += 1
