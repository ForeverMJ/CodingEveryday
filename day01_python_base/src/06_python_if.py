# if
# 判断，如果年龄大于18岁，打印，我已经成年了

age = int(input('请输入你的年龄： '))

if age >= 18:
    print("我已经成年了")
else:
    print('我没有成年')
"""
格式if 
elif 
else


"""

#案例：成绩
score = int(input('请输入本次考试成绩：'))
if (score) >= 90:
    print("yu")
elif (score) >=80 and score < 90:
    print("liang")
elif score >60 and score < 80:
    print("cha")
else:
    print("bujige")

#案例：判断 行程码是否经过杭州，如果没有经过杭州，则判断是否经过北京，如果都没有你
#判断健康吗是不是绿码   嵌套if
xcm ="guangzhou"
jkm = "lvma"
if xcm != "hangzhou" and xcm !="beijing":
    print("xcm yanzheng tongguo")
    if jkm =="lvma":
        print("tongguo")
    elif jkm =="huangma":
        print("butongguo")
    else:
        print("butongguo")
else:
    print('yanzheng butongguo')

'''
python是基于if的特殊表达式格式来模拟三元方案
格式 条件成立的代码 if 判断条件 else 条件不成立代码

'''

res = "成年" if age >= 18 else "未成年"
print(res)