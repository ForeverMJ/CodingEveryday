'''

   定义字符串：
   a = ''
   a = ""

'''

name = 'itcast itheima boxufffeguuuuu'

#字符串都是有下标（索引），下标从0开始 可以通过下标来获得对应数据

print(name[5])

#字符串的切片：可以边界获取某个范围内的字符串）
#列表和元组都支持 切片操作

email = '3345342@gmail.com'
print(email[0:7]) #3345342
print(email[8:])  #gmail.com
print(email[0:-1])

# 字符串的常见的API
print('----------')
words = 'hadoop hive sqoop kafka oozie hue'
#1-- 查找： find() index()
# find(),返回的值为-1时，表示查询内容不存在
print(words.find('hue'))
print(words.find('sqoop',20,50))# -1表示不存在
print(words.find('sqoop',0,50))

# print(words.index('dhsidhi'))# 查询不到直接报错

#2------ relpace (替换前，替换后，替换多少)， split()
print(words.replace('o', 'l', 5))
print(words.split(' '))#默认被空格切割
print(words.split())#默认为所有的空字符包括空格，换行符（/n），制表符（/t）切割
#3--- strip 删除左右两端的空格
print('----------------------')
name = '  itcaste    '
print(name.strip())

