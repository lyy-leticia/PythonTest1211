# #for循环
# a="大哥在哪里"
# for i in a:
#     print(i)

# b=("2","e","f",224,2)
# for i in b:
#     print(i)
#     print("=======")

# #字典
# account={"username":"小乐","sex":"male"}
# for i in account:
#     print("打印键",i)
#     # account["username"]
#     # account[i]
#     #变量i替代常量
#     print("get获值",account.get(i))

# #range
# for i in range(1,10):#前实后空
#     print(i,end=" ")
# print("")

# # range(开始，结束)#前实后空
# a = ['a','b','c', 'd', 'e', 'f', 'g', 'h', 'j','k', 'l']
# for i in range(1,len(a)+1):#len(a)长度
#     print(a[i-1],end=" ")

a = ['a','b','c', 'd', 'e', 'f', 'g', 'h', 'j','k', 'l']
# for i in range(0,len(a)):#len(a)长度
#     print(a[i],end=" ")

# #开始 = 0,结束 = len(a) = 11 > 0-10
# for i in range(len(a)):
#     print(a[i])

# # 第三个参数：步长：每一次隔多少个数
# for i in range(0, 11, 2):
#     print(i)

# #break
# for i in range(10):
#     if i==5:
#         break
#     else:
#         print(i)

# #continue
# # continue
# for i in range(10): #（0,9) i = 0....9

#     if i == 2:
#         continue
#     elif i == 5:
#         break

#     print(i)

# 循环嵌套 99乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{} * {} = {}\t".format(i, j, i*j), end='')       # end=''阻止换行
#     print('')           # 换行， print('')python会自动的添加\n进行换成

for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}\t".format(i,j,i*j),end="")
    print("")

#冒泡排序
    

# i = 1; j = 1-9
# i = 2; j = 1-9
#while