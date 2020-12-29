# account={"username":"lyy","password":"123456"}
# u=input("请输入账号：")
# p=input("请输入密码：")

# if u==account["username"] and p==account["password"]:
#     print(account["username"],"上线了")
# else:
#     print("账号或密码错误")

#p26 02作业
##练习作业:
# 1.用户注册 {"user1":"az"},输入一个账号,如果账号存在,就注册失败,否则就添加一个键值对
# {"user1":"az", "user2":"aq"}

# 2.修改密码,{"username":"az", "password":"123456"},输入一个账号和密码,如果账号正确,就修改密码,
# 否则就提示修改失败

# 3.请输入一个字母,如果输入的字母是大写,就打印:大写, 否则就打印小写
# a > 小写
# A > 大写

# 4.开发敏感词过滤程序,用户输入内容,如果输入的内容包含苍老师,则内容显示 ****xxx
# 苍老师真好看 > ***真好看

# #作业1：
# account={ "user2":"aq"}
# print(account)
# a=input("请输入注册的账号（tip：user1）：")
# b=input("请输入注册的账号昵称（tip：az）：")
# account[a]=b
# print(account)

# #作业2：
# account={"username":"az", "password":"123456"}
# a=input("请输入需要修改密码的账号名（tip：az）：")
# b=input("请输入修改的密码（tip：！=123456）：")
# print("你输入了：",a,b,"旧账号和密码是：",account)
# if a==account["username"]:
#     account["password"]=b
#     print("输入账号正确，密码修改成功。以下是账号和密码：")
#     print(account)
# else:
#     print("输入的账号错误，修改密码失败")

# #作业3：
# big={"A","B","C"}
# small={"a","b","c"}
# a=input("请输入一个字母（tip：abc三选一）：")
# if a in big:
#     print("大写")
# else:
#     print("小写")

#作业4：
minword="苍老师"
a=(input("请输入你要发送的弹幕："))
print("这是您输入的弹幕：",a)
b=a.count(minword)
if b>=1:
    c=a.replace("苍老师","***")
    print("你输入的弹幕含有敏感字，这是您输入的弹幕：",c)
else:
    print(a)