# 演示一个异常的案例
'''
 尝试只读方式打开test。txt文件，如果文件存在则读取文件内容，文件不存在则提示用户
 2。读取内容要求：尝试循环读取内容，读取过程中如果检测到用户意外终止程序，则except捕获异常并提示用户。

'''
import time

try:
    f = open('../data/test.txt','r')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break

            time.sleep(2)
            print(content)
    except:
          print('程序意外被中止')
    finally:
        f.close()
        print('运行完成后，必须指定关闭文件')

except:
    print('文件不存在。。')

