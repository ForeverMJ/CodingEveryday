# 演示io的案例：
# 需求： 用户输入一个文件名，将用户输入的文件名对应的文件进行copy
#形成一个新的文件，新文件格式： 文件名【备份】.后缀

# 1- 接受用户输入的目标文件名
file_name = input('请输入您要备份的文件名：')

# 2- 产生一个新的文件名
index = file_name.rfind('.')

fileName = file_name[0:index]

new_fileName = fileName +'[备份]' + file_name[index:]

print(new_fileName)
