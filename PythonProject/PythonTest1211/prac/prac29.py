import base64
image='1.png'
strchinese = '人生苦短，我用Python!'
bytes = strchinese.encode()
print(type(bytes))
print(len(bytes))
a = bytes
missing_padding =3 - len(a) % 3
if missing_padding:
    a += b'=' *missing_padding
    a=a*700
b = base64.b64decode(a)
print(b) # b'hello'
print(len(a))
# str=b
file_str=open('5.png','wb')
file_str.write(b)
file_str.close()#输出的图片不支持打开？应该去看看数字图像！

# 方法二
#将图片转换成二进制
# f=open(image,'rb')
# f_str=base64.b64encode(f.read())
# f.close()
# print(type(f_str))#<class 'bytes'>
# str=f_str#str二进制bites
# file_str=open('3.jpg','wb')
# file_str.write(base64.b64decode(str))#str二进制bites，编码
# file_str.close()