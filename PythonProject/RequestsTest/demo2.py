#post请求
import requests
from dbtools import query

u ='http://zzy.testgoup.com/api/regist'
d = {"username":"liuyun160","password":"a12345678"}
res =requests.post(url=u,json=d)#指定内容传送

print(res.text)
assert res.status_code == 200
assert res.json()["status"] == 200
#数据库查询
sql="select * from tb_user where username ='{}' and password='{}'".format(d["username"],d["password"])
r=query(sql)
assert len(r) !=0  # len(r) != 0 > 返回值有数据> sql查到了数据 > 账号和密码在数据库 # len(r) == 0 》 账号和密码不在数据库