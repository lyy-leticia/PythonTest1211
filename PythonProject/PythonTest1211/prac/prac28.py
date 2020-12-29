import base64
image='1.png'
 
#将图片encode为二进制字符串方法一
# with open(image,'rb') as f:
#     str=base64.b64encode(f.read())
# print(type(str))#<class 'bytes'>
# print(str)
# 方法二
f=open(image,'rb')
f_str=base64.b64encode(f.read())
f.close()
print(type(f_str))
str=f_str
print(len(str))#19788，可以被2，3,4整除，8不能
result=len(str)%8
print(result)
# file_str=open('4.jpg','wb')
# file_str.write(base64.b64decode(str))
# file_str.close()
