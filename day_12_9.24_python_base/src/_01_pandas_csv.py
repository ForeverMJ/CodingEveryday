import pandas as pd
# 演示 读取CSV格式数据 以及写入到CSV文件中

# 1- 读取外部文件数据
df = pd.read_csv('../data/stu.txt',sep=' ')

# 2- 对数据进行处理操作:  过滤出 年龄大于20岁
df = df[df.age > 20]

# 3- 将处理后写入到csv文件中
df.to_csv('../data/s_age1.txt',index=False,sep='|')


df = pd.read_csv('../data/s_age.txt',sep=',',index_col='Unnamed: 0')
print(df)