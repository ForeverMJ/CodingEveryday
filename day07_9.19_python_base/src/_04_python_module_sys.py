# 演示 sys模块的作用
import sys
# 1- 从外部读取相关的参数 在将python用于脚本的，此操作会非常方便
# print(sys.argv)
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])


# 2- 获取当前执行平台
print(sys.platform)

# 3- 强制退出程序
sys.exit(1)


