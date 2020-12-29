#使用python做http请求
import requests
##1、构造请求
#地址使用字符串表示
u='http://zzy.testgoup.com/api/get/bannerlist'
res=requests.get(u) # requests.get(u) get请求接口；res = 获取所有的响应信息（响应头+返回值）
# print(type(res.text))#打印返回值，固定的res.text

##2、判断结果
#2.1判断http状态码
#2.2判断结果码
assert res.status_code ==200  #判断状态码=200
assert res.json()["status"] ==200   #res.json()把返回值字符串转换成字典
# print(type(res))

##3、数据库查询
#留着,用pymysql包
