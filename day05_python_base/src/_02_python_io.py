#演示文件基本操作
'''
操作文件一般有三个步骤：
   1- 打开文件
   2- 对文件执行相关操作
   3- 关闭文件

'''

# 1- 打开文件
# w 表示写入操作，当文件不存在的时候，直接创建，如果文件存在，会删除元文件
# a 表示追加写入，如果文件不存在，直接创建，如果文件不存在会在尾部继续追加
# r+ ：支持读写操作，如果文件不存在，会直接报错，写入的时候，会将对应位置的数据替换掉
f = open('../data/a.txt','w')

# 2- 执行写入操作
f.write('hello python')

# 3- 关闭文件
f.close()

# 演示读取数据的操作
f = open('../data/c.txt','r') #  默认模式就是r 只读模式

# res = f.read(1024)
#
# print(res)
#
# res = f.read(10)
#
# print(res)

res = f.readline(1) #只读第一行数据，参数可指定读取1行的前N个数据
print(res)
res_list = f.readline()
print(res_list)





