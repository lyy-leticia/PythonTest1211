# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# print(len(a))#5
# for i in range(len(a)):#0-4
#     print(i, a[i])
# b=list(range(5))#范围5，输出0-4
# print(b)

# #break跳出循环，continue跳出本循环
# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         break
#     print(n)
# print('循环结束。')

# u=5
# while u > 0:
#     u -= 1
#     if u == 2:
#         continue
#     print(u)
# print('循环结束。')

# for letter in 'Runoob':     # 第一个实例,python中的变量如letter不需要提前定义
#    if letter == 'b':
#       break
#    print ('当前字母为 :', letter)
  
# var = 10                    # 第二个实例
# while var > 0:              
#    print ('当期变量值为 :', var)
#    var = var -1
#    if var == 5:
#       break
 
# print ("Good bye!")

# for letter in 'Runoob':     # 第一个实例
#    if letter == 'o':        # 字母为 o 时跳过输出
#       continue
#    print ('当前字母 :', letter)
 
# var = 10                    # 第二个实例
# while var > 0:              
#    var = var -1
#    if var == 5:             # 变量为 5 时跳过输出
#       continue
#    print ('当前变量值 :', var)
# print ("Good bye!")

for n in range(2, 10):#2-9,前实后空
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')