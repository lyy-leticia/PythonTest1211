# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1#python可以同时赋值

while b < 10:
    print(b)
    a, b = b, a+b