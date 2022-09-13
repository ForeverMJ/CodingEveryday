"""

      break: 立刻跳出当前循环
      continue： 跳出本次循环，进入下一次循环


"""
name = 'boxuegu'

for i in name:
    if i == 'u':
        print('遍历到u了')
        break

    print(i)
else:
    print('执行到else')

#while 循环中
i = 1
while i <= 5:
    if i > 3:
        break

    print(i)
    i += 1
else:
    print('xxxxxxxx')

#continue
print('------------------------')
# 在while中如何使用，打印1-6，不打印3
i = 0
while i <= 6:

    i += 1
    if i == 3:
        continue
    if i == 7:
        break
    print(i)

