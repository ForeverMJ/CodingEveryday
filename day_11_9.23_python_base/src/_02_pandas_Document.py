# 使JupyterNotebook单个cell可以有多个输出
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

#
import pandas as pd
# 构造数据集

df = pd.DataFrame(
    [
        ['1960-5-7','liu','职业法师'],
        ['1978-9-1', '赵金龙', '大力哥'],
        ['1984-12-27', '周立齐', '窃格瓦拉'],
        ['1969-1-24', '于谦', '相声皇后']
    ],
    columns=['birthday', 'name', 'AKA']
)

print(df)

# 写入csv文件

df.to_csv('./写文件.csv')
# 此时应该在运行代码的相同路径下就生成了一个名为“写文件.csv”的文件
# 执行`df.to_csv()`时，文件需要关闭才能写入，不然会报 `PermissionError:
# [Errno 13] Permission denied: 'xxxx.csv'`的异常

# 读文件
dfread = pd.read_csv('./写文件.csv')
print(dfread)

'''
index_col 参数指定索引

```
index_col参数可以在读文件的时候指定列作为返回dataframe的索引，两种用法如下:
* 通过列下标指定为索引
* 通过列名指定为索引
```

'''

# 通过列下标指定为索引`index_col=[列下标]`
df5 = pd.read_csv('./写文件.csv', index_col=[0])
print(df5)

# 通过列名指定为索引`index_col=['列名']`
df = pd.read_csv('./写文件.csv',index_col=['Unnamed: 0'])
print(df)
