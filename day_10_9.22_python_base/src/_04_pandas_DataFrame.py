'''
DataFrame的创建有很多种方式

- Serires对象转换为df：上一小节中学习了`s.to_frame()`以及`s.reset_index()`
- 读取文件数据返回df：在之前的学习中我们使用了`pd.read_csv('csv格式数据文件路径')`的方式获取了df对象
- 使用字典、列表、元组创建df：接下来就展示如何使用字段、列表、元组创建df
'''

# 使用字典➕列表创建df，默认自增index
import pandas as pd

df1_data = {
    'date': ['2021-08-08','2020-07-07','2022-08-09'],
    'temp': [25,26,27],
    'humidity':[81,50,60]

}
df1 = pd.DataFrame(df1_data)
print(df1)

# 使用列表加元组创建df，并自定义索引
df2_data = [
    ('2021-08-21', 25, 81),
    ('2021-08-22', 26, 50),
    ('2021-08-23', 27, 56)
]
df2 = pd.DataFrame(
    data= df2_data,
    columns=['data','temp','humidity'],
    index = ['row_1','row_2','row_3']
)
print(df2)


# 返回df的函数
print(len(df2))

# df中数据的个数
size = df2.size
print(size)

# df中的行数和列数，元组 (行数, 列数)
print(df2.shape)

# 返回列名和该列数据的类型
print(df2.dtypes)

# 返回nparray类型的2维数组，每一行数据作为一维数组，所有行数据的数组再构成一个二维数组
print(df2.values)

# 返回df的所有列名
print(df2.columns)

# df遍历返回的只是列名
for col_name in df2:
    print(col_name)

# 返回df的索引对象
print(df2.index)

# 返回第一行数据，默认前5行
print(df2.head(1))

# 返回倒数第1行数据，默认倒数5行
print(df2.tail(1))

# 返回df的基本信息：索引情况，以及各列的名称、数据数量、数据类型
print(df2.info()) # series对象没有info()方法

# 返回df对象中所有数字类型数据的基础统计信息
# 返回对象的内容和Series.describe()相同
print(df2.describe())

# 返回df对象中全部列数据的基础统计信息
print(df2.describe(include='all'))

