import pandas as pd
# 构造一个series对象

s4 = pd.Series([i for i in range(6)], index=[i for i in 'ABCDEF'])

# series和数值型变量计算
num1 = s4 * 5
print(num1)
print('-'*20)
# 两个series对象相加
s5 = pd.Series([10]*6, index=[i for i in 'ABCDEF'])
print(s5)
print('-'*20)
num2 = s4 + s5
print(num2)
num2

# 索引不同的两个s对象运算
s6 = pd.Series([10]*6, index=[i for i in 'ABCDEG'])
print(s6)
print(s4 + s6)


