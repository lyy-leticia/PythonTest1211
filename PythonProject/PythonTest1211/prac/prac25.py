import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
 
x = np.arange(28*28)  # 生成数组
# print(x)
result = x.reshape((28, 28))  # 将一维数组变成28行28列  原数组不会被修改或者覆盖
# print(result)
# #img_train = pd.read_csv(x)#读取kaggle数据集，一维数组，代表28*28的图像
img_train = np.array(x)#这个是关键，转化为数组##本来就是数组了
print(img_train)
trainSet = np.zeros((28, 28))#生成0
# print(trainSet)
trainSet2 = np.zeros((1, 784))
# print(trainSet2)#变一维数组
t =img_train[0][1:]
# print(t)
trainSet=img_train.reshape(28, 28)
 
print(trainSet)
pyplot.imshow(trainSet)
pyplot.show()