import array
a=input("请输入您的英文名")
print(type(a))
b=a.encode()#字符串转字节
print(b)
last=[i for i in b]
print(last)