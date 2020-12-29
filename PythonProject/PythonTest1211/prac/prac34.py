import re
# import numpy as np
import array
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

a=input("请输入您的英文名(8个字符以内）")
            # a="xxxxxxx"
b=a.encode()#字符串转字节
print(type(b))
print(b)
x=[i for i in b]#这是列表
print(x)