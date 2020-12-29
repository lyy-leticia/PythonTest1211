def encode(s):
 
    #实现字符串转换成二进制表示
    #字符串 -> ASCII码数值 -> 二进制表示
    ###str_bin = ' '.join([bin(ord(c)).replace('0b', '') for c in s]) 该代码可转换成裁开的for 循环，如下四行代码：
 
    tmp = []
    for c in s:
        tmp.append(bin(ord(c)).replace('0b', ''))
 
    str_bin = ' '.join(tmp)
    
 
    return str_bin

def decode(s):
# 实现二进制表示转换成字符串表示
# 二进制表示 -> ASCII码数值 -> 字符串表示
    bin_str = ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
 
    return bin_str

a=encode("lyy")
print(a)
print(decode(a))




# import numpy as np
# import matplotlib.pyplot as pyplot 
# x = np.arange(64)  # 生成数组
# print(x)
# result = x.reshape((8, 8))  # 将一维数组变成4行5列  原数组不会被修改或者覆盖
# print(result)
# # x.resize((2, 10))  # 覆盖原来的数据将新的结果给原来的数组
# # print(x)
# # a=pyplot.imshow(result)
# # print(a)
# myarr = np.asarray(result)
# img = image.fromarray(myarr, "I")
# img.save("my.png")