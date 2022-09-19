# 演示 python的模块的导入方案
'''
支持的导入方式
     import 模块名
     from 模块名 import 功能名
     from 模块名 import *
     import 模块名 as 别名
     from 模块名 import 功能名 as 别名
'''
# 方式一： 这种方式，相当于直接把某个模块下 所有的内容全部都导入进来，后续可以使用模块名.API


import math

print(math.ceil(3.8))

# 方式二： 这种方式，相当于直接把某个模块下 所有的内容全部导入进来，并给模块起一个别名    后续可以使用别名.API

import math as  m
print(m.ceil(3.9))

# 方式三： 导入某一个模块中指定的功能，后续使用的时候，可以直接使用功能名称
from math import ceil,floor

print(ceil(3.8))
print(floor(3.8))

#方式四： 将这个模块的全部功能导入，后续可以直接使用功能名称

from math import *
print(ceil(3.8))
print(floor(3.8))

# 方式五： 导入模块的具体功能，并给这个功能名称起一个别名
# 别名的意义： 不通模块下的相同名称的功能，为了区分，取别名
from math import ceil as c

print(c(3.8))




