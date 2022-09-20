# 综合案例： 学生管理系统
import sys


def system_ui():
    print('-' * 30)
    print('1: 添加学员')
    print('2: 删除学员')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 显示所有学员信息')
    print('6: 退出系统')


info_stu = []  # 容器用来存放学生数据


# 添加学员功能
def add_stu():
    # 接收用户输入学员信息
    stu_id = input('请输入学号')
    stu_name = input('请输入姓名：')
    stu_address = input('请输入地址')

    # 声明info_stu是全局变量
    global info_stu

    # 检测用户输入的姓名是否存在，存在则报错提示
    for stu in info_stu:
        if stu_id == stu['name']:
            print('该用户已存在,添加失败')
            return

    # 如果用户输入的姓名不存在，则添加该学员的信息
    info_stu.append({'sid': stu_id, 'name': stu_name, 'address': stu_address})
    print(info_stu)

# 删除学员功能： 根据学员的id来删除学员
def del_stu():
    # 用户输入要删除的学员的id号
    sid = input('请输入要删除学员的学号：')

    global info_stu
    for stu in info_stu:
        if sid == stu['sid']:
            # 说明存在需要删除
           info_stu.remove(stu)
           break
    else:
        print('该学号不存在')

    print(info_stu)

# 修改学员信息：
def update_stu():
   # 1-输入需要修改的学员学号
     sid = input('请输入需要修改的学员学号：')
   # 2-判断学员是否存在
     for stu in info_stu:
         if sid == stu['sid']:
             print(sid)
             num = input("请问，是修改姓名还是地址呢（0，1）？")
             if num == '0':
                 name = input("请输入需要修改的姓名")
                 stu['name'] = name
             elif num == '1':
                 address = input("请输入需要修改的地址")
                 stu['address'] = address
             break

     else:
            print('该学员不存在，无法执行修改操作，请先添加学员')
print(info_stu)


# 查询学员信息 根据姓名来查询学员信息 （学员姓名可能会重复）
def search_stu():
    name = input('请输入需要查找的学员姓名')

    global info_stu
    # 遍历学员列表，找出学员信息
    stu_list = []
    for stu in info_stu:
        if name ==stu['name']:
            stu_list.append(stu)

    # 判断列表是否为空：
    if len(stu_list) >0:
        print('查询到一些学员信息：')
        for stu in stu_list:
            print(f'学员信息为：{stu["sid"],stu["name"],stu["address"]}')
    else:
            print("未找到任何学员的信息")

    # 显示所有的学员信息
def find_all():
    print('学号\t姓名\t地址')
    for stu in info_stu:
        print(f'{stu["sid"],stu["name"],stu["address"]}')









while True:
    system_ui()
    # 2- 用户选择功能
    user_num = input('请选择您需要执行的功能序号：')
# 3- 根据用户选择，执行不同功能
    if user_num == '1':
      add_stu()
    elif user_num == '2':
      del_stu()
    elif user_num == '3':
      update_stu()
    elif user_num == '4':
      search_stu()
    elif user_num == '5':
      find_all()
    elif user_num == '6':
      exit = input('您确定要退出吗(yes or no)?')

      if exit == 'yes':


        sys.exit(0)


    else:
      print('输入错误，请重新输入')
