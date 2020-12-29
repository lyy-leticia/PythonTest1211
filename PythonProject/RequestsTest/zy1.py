# day1作业
# 1.使用requests完成登录接口的完整测试流程，自己写！！！

# 2.登录>领取任务  (选做)还没做
import requests
from dbtools import query
from filetools import write_file, read_file

uu ='http://zzy.testgoup.com/api/login'
dd = {"username":"liuyun117","password":"a12345678"}

res1 =requests.post(url=uu,json=dd)#指定内容传送
# print(res1.text)
# print(type(res1.text))
assert res1.status_code == 200
assert res1.json()["status"] == 200
# 数据库查询
sql="select * from tb_user where username ='{}' and password='{}'".format(dd["username"],dd["password"])
r=query(sql)
assert len(r) !=0  
# len(r) != 0 > 返回值有数据> sql查到了数据 > 账号和密码在数据库 # len(r) == 0 》 账号和密码不在数据库
print("登陆成功")

#python的关联
uid=res1.json()["data"]["id"]
token=res1.json()["data"]["token"]
# print(token)
write_file('./conf/user_token.txt', res1.json()["data"]["token"])
write_file('./conf/user_id.txt', str(res1.json()["data"]["id"]))
# 文件读写的方式，写入到txt中

print("------领取任务--------")
url2="http://zzy.testgoup.com/api/receive/taskinfo"
data2={"id":"4761"}
header={"token":token}
res=requests.post(url=url2,json=data2,headers=header)

assert res1.status_code == 200
assert res1.json()["status"] == 200

sql="select * from tb_user_task where taskid={} and uid={}".format(data2["id"],uid)
t=len(query(sql))
assert t != 0

print("领取任务成功")
