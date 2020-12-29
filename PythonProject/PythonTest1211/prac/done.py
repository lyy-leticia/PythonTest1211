import matplotlib.pyplot as pyplot
import random
import numpy as np
import array

pyplot.figure(num='英文名的图片',figsize=(8,8))  #创建一个名为astronaut的窗口,并设置大小

#有个问题
a=input("请输入您的英文名(只限7个字符）")
# print(type(a))#<class 'str'>
b=a.encode()#字符串转字节
# print(b)#b'leticia'
x=[i for i in b]#这是列表
#调整列表长度为28*28
if len(x)<8:
    x.append(0)
    print(x)
n=(28*28)/8
n=int(n)
xx=x*n
xx = np.array(xx)#将列表转一维数组
# # x = np.arange(28*28)  # 生成一维数组#我要输入的字符串
# print(type(x))
# np.random.shuffle(x)#将一维数组的顺序随机打乱
# # print(x)
im_mask = xx.reshape((28, 28))  # 将一维数组转成二维数组28行28列  原数组不会被修改或者覆盖
# print(type(im_mask))#<class 'numpy.ndarray'>
# print(im_mask)
pyplot.imshow(im_mask, pyplot.cm.summer)#图片输出，颜色设置
pyplot.show()#图片展示

#颜色设置winter,summer,autumn,gray