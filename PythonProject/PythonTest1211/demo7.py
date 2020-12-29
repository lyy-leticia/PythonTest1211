#作业
# print("请输入一个年龄（33）：")
# age=input()
# print("您输入的年龄是：",age)

# a="迪迦"
# b="的年龄是"
# c=a+b+age
# print(c)

# d=[c]
# print(d)

# str2="奥特曼"

# d.append(str2)
# print(d)

# e=d.count("奥特曼")
# print(e)

#p26python入门02周五课程
#字典
# a={}
# # #没有任何元素/键值对的字典
# print(type(a))
a={"username":"leticia","age":18,"sex":"female","phone":"123456"}
#取值
# print(a["username"])
# print(a.get("username"))#get方法取值
# #print(a["username1"])#报错
# print(a.get("username1"))#不报错，返回none

#增加/修改
a["3D"]="123123123"
print(a)
a["sex"]="male"
print(a)

#删除
del a["3D"]
print(a)

#清空
a.clear()
print(a)
#内容的嵌套
b=[1,2,3]
c={"list":b}
print("c is",c)

d={
    "data":{"token":"123434671"},
    "msg":"登录成功",
    "status":200
}
print("d is",d)


