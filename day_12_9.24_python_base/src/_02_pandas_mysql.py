import pandas as pd
from sqlalchemy import create_engine
# 演示: 如何将数据写入到MySQL中
df = pd.read_csv('../data/stu.txt',sep=' ')

print(df)

# 将数据写入到MySQL
conn = create_engine('mysql+pymysql://root:123456@192.168.88.161:3306/day05_python?charset=utf8')

df.to_sql('stu_pandas',conn,if_exists='replace',index=False)

# 如何读取数据
df = pd.read_sql('select sid,name,address from stu_pandas',conn,index_col='sid')
print(df)