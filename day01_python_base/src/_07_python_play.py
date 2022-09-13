#猜拳游戏
# 假设 石头为1 剪刀为2 布为3
#1—— 定义电脑出拳内容，假设只会出石头
import  random
computer = random.randint(1,3)

#2- 定义用户要输出什么内容
user = int(input('请选择要出什么：石头为1 剪刀为2 布为3'))
#3-比较哪方赢了
if user == computer:
    print('ping'+',电脑出了：'+str(computer))
elif (user ==1 and computer == 2) or (user == 2 and computer ==3) or (user == 3 and computer == 1):
    print('ying'+',电脑出了：'+str(computer))
else:
    print('shu'+',电脑出了：'+str(computer))