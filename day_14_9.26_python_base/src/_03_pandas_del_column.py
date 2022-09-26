# 演示pandas的增删改查: 删除列 去重

import pandas as pd

df = pd.read_csv('../data/stu.txt',sep=' ')

df2 = df.copy()


# 1- 删除行
df2 = df2.drop([0,3])    # 删除第0 和第3行

print(df2)

# 2- 删除列
df2 =df2.drop(['sex'],axis=1)     # 如果添加参数`axis=1`，则删除指定列名的列
print(df2)

# del df2['age']     # 永久删除文件，慎重

# print(df2)

# 3- 去重处理
df2 = df.copy()


# reset_index 用于重置索引, 因为append后 新的df的所有还会保持原样
df2 = df2.append(df).reset_index(drop=True)
print(df2)

df2 = df2.drop_duplicates()    # 实施去重操作

print(df2)