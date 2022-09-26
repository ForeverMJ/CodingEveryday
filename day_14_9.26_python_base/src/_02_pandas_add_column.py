# 演示pandas的增删改查: 增加列

import pandas as pd

df = pd.read_csv('../data/stu.txt',sep=' ')

df2 = df.copy()
# 方式一 通过直接赋值方式增加
df2['birthday'] = '2020-10-10'
df2['birthday'] = ['2020-10-10','2021-10-10','2019-10-10','2020-09-10','2020-10-12','2020-12-10','2020-08-10']
df2['a'] = df2['age'] * 2
print(df2)
print('-'*50)
# 方式二: 通过 assign增加列, 不会改变原有, 每次都会产生一个新的df
df2 = df.copy()

df2 = df2.assign(b=100)
df2 = df2.assign(c=[1,2,3,4,5,6,7])
# 一次性增加多列
df2 = df2.assign(d=[1,2,3,4,5,6,7],e=[1,2,3,4,5,6,7])
print(df2)