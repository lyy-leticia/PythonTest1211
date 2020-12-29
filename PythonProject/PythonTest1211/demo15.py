# #练习：成绩分组，把合格的、不合格的单独分组

# grade ={"qiuguo":58,"dengyuan":80,"jiale":68,"qingyi":48}
# a,b=[],[]
# for i in grade:#键
#     if grade[i]>59:
#         a.append(i)#键
#         #放进合格数组
#     else:
#         b.append(grade[i])#值
#         #放进不合格
# print(a)
# print(b)

#红绿灯
# for i in range(60):
#     if i<25:
#         print("hongdeng")
#     elif i<55:
#         print("lvdeng")
#     else:
#         print("huangdeng")
# 等待:包
import time # 导入，要使用包，就必须要先导入

while True:
    for i in range(60):
        if i < 25:
            print("\033[1;31m 红灯\033[0m")
        elif i < 55:
            print("\033[1;42m 绿灯\033[0m")
        else:
            print("\033[1;33m 黄灯\033[0m")

        time.sleep(1)