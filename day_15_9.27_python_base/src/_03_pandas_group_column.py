# 演示pandas的分组

import pandas as pd

df = pd.read_csv('../data/stu.txt',sep=' ')

# 执行分组:
print(df.groupby(['address']).first()) # 获取每组的第一个
print(df.groupby(['address']).last())  # 获取每组的最后一个

print(df.groupby(['address','sex']).first())
print(df.groupby(['address','sex']).last())

print(df.groupby(['address', 'sex']).get_group(('广州', '男')))

# 聚合计算
print(
    df.groupby(['address', 'sex']).agg({
        'sid': 'count',
        'age': 'sum'
    })
)

# 过滤操作
print(df.groupby(['address']).filter(lambda df_g: df_g['age'].mean() > 23))

# 分组中，平均年龄大于23岁