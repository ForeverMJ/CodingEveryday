# 演示 python的异常处理的操作
'''
    异常捕获的基本格式：
        try:
           书写可能发生异常的代码
        except:
           如果出现异常，执行的代码


'''

try:
    f = open('../data/e.text','r')
except:
    print('出现了异常')
    f = open('../data/e.txt','w')

'''
    支持捕获指定异常：
        try:
           书写可能发生异常的代码
        except 异常类型:
           如果出现异常，执行的代码


'''
try:
    f = open('../data/f.txt','r')
except (ZeroDivisionError,FileNotFoundError) as exc:
    print(f'捕获到 除0/或者文件不存在的异常，异常信息为:{exc}')

# 捕获所有的异常

try:
    f = open('../data/f.txt','r')
except Exception as rxc:
    print(f'捕获到 除0/或者文件不存在的异常，异常信息为:{rxc}')

# 异常中带有else
'''
   try:
           书写可能发生异常的代码
        except 异常类型:
           如果出现异常，执行的代码
    else：
        整个代码没有任何异常的时候，指定的内容

'''
try:
     f = open('../data/a.txt','r')
except Exception as rxc:
     print(f'捕获到 除0/或者文件不存在的异常，异常信息为:{rxc}')
else:
    print('本次执行没有任何异常')

# finally:  不管是否有异常，都要指定的内容
try:
    f = open('../data/a.txt','r')
except Exception as rxc:
     print(f'捕获到 除0/或者文件不存在的异常，异常信息为:{rxc}')
else:
    print('本次执行没有任何异常')
finally:
    print('有没有异常，都要执行')
    f.close()


