# 演示io的案例：
# 需求： 用户输入一个文件名，将用户输入的文件名对应的文件进行copy
#形成一个新的文件，新文件格式： 文件名【备份】.后缀

# 1- 接受用户输入的目标文件名
file_name = input('请输入您要备份的文件名：')

# 2- 产生一个新的文件名
index = file_name.rfind('.')  # rfind是从后往前找

fileName = file_name[0:index]  # 从0开始找到.之前的名字，可以直接捕获文件名

new_fileName = fileName +'[备份]' + file_name[index:]

print(new_fileName)

# 3- 将原有文件内容，完整的写入到新的文件中，从而完成拷贝工作
old_f = open(f'../data/{file_name}','rb')   # rb是字节的读取方案
new_f = open(f'../data/{new_fileName}','wb')

while True:
    content = old_f.read(1024)

    if len(content) == 0:
        break

    new_f.write(content)

# 4- 关闭资源
old_f.close()
new_f.close()
