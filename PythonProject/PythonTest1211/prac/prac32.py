import array
a=input("请输入您的英文名")
print(type(a))
b=a.encode()#字符串转字节
print(b)
# #字节转16进制的字符串
# c=b.hex()
# print(type(c))
# print(c)
# #16进制的字符串转int
# d=int(c,16)
# print(d)
# print(type(d))

last=[i for i in b]
print(last)

# array.array('B', c)

# arr = ['123']
# arr = list(d)
# print(arr)

# #[22, 44, 66, 88]