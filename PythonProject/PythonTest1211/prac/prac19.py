# # 可写函数说明
# sum = lambda arg1, arg2: arg1 + arg2
 
# # 调用sum函数
# print ("相加后的值为 : ", sum( 10, 20 ))
# print ("相加后的值为 : ", sum( 20, 20 ))

# jian = lambda a,b:a-b#更简单的函数定义，lambda
# print(jian(20,10))

# #如果单独出现星号 * 后的参数必须用关键字传入。
# def f(a,b,*,c):
#      return a+b+c
# print(f(1,2,c=3)) # 正常

#参数,形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参:
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
f(10, 20, 30, d=40, e=50, f=60)
#return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。
#如果我们需要从 math 模块中输出 pi 常量，以下代码正确的是？
#from math import pi
#print(pi)