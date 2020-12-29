#数组:长度可变的元组

a=[1,2,3,4,5,6]
print(type(a))

#取值
print(a[5])
print(a[-1])
print(a[1])

#添加
a.append(7)
print(a)

a.insert(3,1000)
print(a)

#修改元素
a[0]=100
print(a)

#删除
del a[-1]
print(a)

a.remove(6)
print(a)

#len
print("输出数组：")
print(a)
print("输出数组长度len：")
print(len(a))

#统计出现次数
b=a.count(100)
print(b)

#排序
a.sort()#从小到大
print("从小到大排序输出：")
print(a)
print("排序反转输出：")
a.sort(reverse=True)
print(a)

print(sum(a))