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

'''
 当DataFrame和数值进行运算时，DataFrame中的每一个元素会分别和数值进行运算，
 但df中的数据存在非数值类型时不能做加减法运算

两个DataFrame之间、以及df和s对象进行计算，和2个series计算一样，
会根据索引的值进行对应计算：当两个对象的索引值不能对应时，不匹配的会返回NaN
 
'''
print(df2 * 2)

# df和df进行运算
print(df2 + df1)    # 索引完全不匹配 返回NaN

# 构造部分索引和df2相同的新df

df3 = df2[df2.index!='row_3']
print(df3)
print('_' *50)
# 部分索引相同
print(df2 + df3)

df1types = df1.info()
print(df1types)


'''
# 可以通过下列API查看s对象或df对象中数据的类型
s1.dtypes
df1.dtypes
df1.info() # s对象没有info()方法
'''


