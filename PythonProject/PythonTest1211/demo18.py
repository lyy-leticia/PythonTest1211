#异常处理,增强代码的健壮性
a=[1,2.3]
try:
    b=a[1]
    print("1")
except:
    print("2")
else:
    print("3")
finally:
    print("4")

# 报错： try > except > finally
# 没报错： try > else > finally