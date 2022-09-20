# 综合案例: 学生管理系统
import sys


def system_ui():
    print('-' * 30)
    print('欢迎登录学生管理系统')
    print('1: 添加学员')
    print('2: 删除学员')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 显示所有学员信息')
    print('6: 退出系统')


info_stu = []  # 此容器用于放置学员信息


# 添加学员
def add_stu():
    # 使用者输入学员信息
    stu_id = input('请输入学员学号:')
    stu_name = input('请输入学员姓名:')
    stu_address = input('请输入学员地址:')

    global info_stu

    # 在添加数据之前, 判断是否有重复的学员
    for stu in info_stu:
        if stu_id == stu['sid']:
            print("学员已存在, 添加失败~~")
            return

    # 如果输入学员不存在, 添加到 info_stu
    info_stu.append({'sid':stu_id,'name':stu_name,'address':stu_address})

    print(info_stu)


# 删除学员 : 根据学员的id来删除学员
def del_stu():
    # 用户输入要删除学员的id号
    sid = input('请输入要删除学员的学号:')

    global info_stu

    # 判断学员是否存在
    for stu in info_stu:
        if sid == stu['sid']:
            # 说明存在, 然后需要删除
            info_stu.remove(stu)
            break
    else:
        print('该学号不存在...')

    print(info_stu)


# 修改学员信息:
def update_stu():
    # 1- 输入要修改的学员学号
    sid = input('请输入要修改学员的学号:')

    global info_stu
    # 2- 判断, 学员是否存在
    for stu in info_stu:
        if sid == stu['sid']:
            print(stu)
            num = input('请问, 是修改姓名还是地址呢(0,1)?')
            if num == '0':
                name = input('请输入修改后的学员的姓名:')
                stu['name'] = name

            elif num == '1':
                address = input('请输入修改后的学员的地址:')
                stu['address'] = address
            break
    else:
        print("学员不存在, 无法执行修改操作, 请先添加学员")

    print(info_stu)


# 查询学员信息 根据姓名来查询学员信息   (学员姓名可能会重复)
def search_stu():
    name = input('请输入要查询的学员的姓名:')

    global info_stu
    # 遍历学员列表, 找出学员信息
    stu_list = []
    for stu in info_stu:
        if name == stu['name']:
            stu_list.append(stu)

    # 判断列表是否为空:
    if len(stu_list) >0:
        print("查询到一些学员信息:")
        for stu in stu_list:
            print(f'学员信息为:{stu["sid"]}, {stu["name"]},{stu["address"]}')
    else:
        print("未查询到任何的学员信息")


# 显示所有的学员信息
def find_all():
    print('学号\t姓名\t地址')

    for stu in info_stu:
        print(f'{stu["sid"]}\t{stu["name"]}\t{stu["address"]}')



while True:
    system_ui()

    user_num = input('请选择您需要执行的功能序号:')

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
            #sys.exit(0)
            # 或者 写break
            break
    else:
        print('输入错误, 请重新输入')

