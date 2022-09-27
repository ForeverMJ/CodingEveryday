# 演示pandas的增删改查: 删除列 去重

import pandas as pd

df = pd.read_csv('../data/stu.txt',sep=' ')

df2 = df.copy()


# 1- 替换列
df2 = df2.assign(sex='男')    # 直接覆盖
print(df2)

# 2- 直接赋值修改
df2['age'] = [1,2,3,4,5,6,7]
print(df2)

# 3- 替换操作
s = df2['name'].replace('王五','老王')  # 默认返回一个新series对象，不对原有数据进行修改

df2['name'].replace('王五','老王',inplace=True)   # 直接修改现有的df
print(s)

print(df2)