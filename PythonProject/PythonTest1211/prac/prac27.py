import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
#数组
x = np.arange(8*8)  # 生成一维数组
print(x)
img_train = x.reshape((8, 8))  # 将一维数组变成28行28列二维数组  原数组不会被修改或者覆盖
print(img_train)
myarr=np.asarray(img_train)
img=Image.fromarry(myarr,"I")
img.save("my.png")