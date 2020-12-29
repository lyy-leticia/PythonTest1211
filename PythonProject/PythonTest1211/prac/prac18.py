# # 可写函数说明
# def changeme( mylist ):
#    "修改传入的列表"
#    mylist.append([1,2,3,4])
#    print ("函数内取值: ", mylist)
#    return
 
# # 调用changeme函数
# mylist = [10,20,30]
# changeme( mylist )
# print ("函数外取值: ", mylist)

# #可写函数说明
# def printme( str ):
#    "打印任何传入的字符串"
#    print (str)
#    return
 
# # 调用 printme 函数，不加参数会报错
# printme("hello")

# #可写函数说明
# def printinfo( name, age = 35 ):
#    "打印任何传入的字符串"
#    print ("名字: ", name)
#    print ("年龄: ", age)
#    return
 
# #调用printinfo函数
# printinfo( age=50, name="runoob" )
# print ("------------------------")
# printinfo( name="runoob" )

# # 可写函数说明
# def printinfo( arg1, *vartuple ):#*不定长元组
#    "打印任何传入的参数"
#    print ("输出: ")
#    print (arg1)
#    for var in vartuple:
#       print (var)
#    return
 
# # 调用printinfo 函数
# printinfo( 10 )
# printinfo( 70, 60, 50 ）
# 
# 
def printinfo( arg1, **vardict ):#**字典
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)