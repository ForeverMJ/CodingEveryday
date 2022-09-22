# 1- 导入pandas的包
import pandas as pd

# 需求： 读取一个外部的文件，存储一个全球GDP文件，请读取这个数据，获取中国地区的GDP数据

# 2- 读取外部的数据
df = pd.read_csv('../data/1960-2019全球GDP数据.csv',encoding='GBK')


# 3- 获取中国的GDP数据
china_gdp = df[df.country == '中国']

print(china_gdp)

# 使用默认自增索引
s2 = pd.Series([1,2,3])
print(s2)

# 自定义索引

s3 = pd.Series([1,2,3], index=['A','B','C'])
print(s3)

# 构造一个series对象

s4 = pd.Series([i for i in range(6)], index=[i for i in 'ABCDEF'])
print(s4)
print('-'*50)
# s对象有多少个值，int
len(s4)
size = s4.size
print(size)
print('-'*50)
# s对象有多少个值，单一元素构成的元组 （6， ）
shape = s4.shape
print(shape)
print('-'*50)
# 查看s对象中数据的类型
types = s4.dtypes
print(types)
print('-'*50)

# s对象转换为list列表
tolist = s4.tolist()
print(tolist)
print('-'*50)
# s对象的值 array([0, 1, 2, 3, 4, 5], dtype=int64)
values = s4.values
print(values)
print('-'*50)

# s对象的值转换为列表
valuestolist = s4.values.tolist()
print(valuestolist)
print('-'*50)

# s对象可以遍历，返回每一个值
for i in s4:
    print(i)
print('-'*50)


# 下标获取具体值
va = s4[1]
print(va)
print('-'*50)

# 返回前2个值，默认返回前5个
head = s4.head(2)
print(head)
print('-'*50)

# 返回最后1个值，默认返回后5个
tail = s4.tail(1)
print(tail)
print('-'*50)

# 获取s对象的索引 Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
index = s4.index
print(index)
print('-'*50)

# s对象的索引转换为列表
indextolist = s4.index.to_list()
print(indextolist)
print('-'*50)

# s对象中数据的基础统计信息
describe = s4.describe()
print(describe)

print('-'*50)

# seriest对象转为df对象

s4.to_frame()
s4.reset_index()
