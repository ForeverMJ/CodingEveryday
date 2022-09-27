# 演示pandas的增删改查:  查询

import pandas as pd

df = pd.read_csv('../data/stu.txt',sep=' ')


# 1- 从前往后取多行数据
print(df.head(3))

# 2- 从后往前取
print(df.tail(3))

# 3- 获取某一列 或者某几列
print(df['sid'])
print(df[['sid','name']])

# 4- 获取某几行数据
print(df[0:2])  # 包头不包尾
print(df[0:5:2]) # 获取第0行到第五行, 步长为2
print(df[3::2]) # 从第三行开始到结束, 步长为2

# 5- 过滤数据
print(df[df.name == '张三'])
print(df.query('name=="张三"'))

# 6- 排序操作
print(df.sort_values(['age'],ascending=False))   # ascending=False，倒序排序

# 7- 聚合操作
print(df['age'].max())     # 按年龄从大到小排序