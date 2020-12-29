def mul(s1,s2):
    return s1*s2


def add(s1,s2):
    sum=s1+s2
    return sum

a=add(1,2)
print(a)
b=add(2,3)
print(b)
c=mul(a,b)
print(c)

# 参数的默认值
def add1(s1=10, s2=20):
    return s1 + s2

a = add1()
print(a)

# 参数类型
def print123(c):
    print(c)#没有return默认返回None

print123({"username":"123"})#参数类型随输入的参数而改变

# 参数的默认值
def add11(s1=10, s2=20):
    return s1 + s2
