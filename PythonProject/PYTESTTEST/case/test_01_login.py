import pytest
import requests

import os,sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import read_file
from utils.filetools import write_file
from utils.exceltools import read_excel

#数据和脚本分离出来，d放到外面作为公用变量
d= read_excel('data/datas.xlsx',"登录")

#登录成功
def test_01_login_success():
    #request请求代码
    url=d[0][2]
    data=eval(d[0][4])
    res = requests.post(url=url,json=data)
    
    print(res.text)
    assert res.status_code ==d[0][6]
    assert res.json()["status"]==d[0][7]

    #sql验证
    sql="select * from tb_user where username='{}' and password = '{}'".format(data['username'],data['password'])
    assert len(query(sql)) !=0

    #关联
    token=res.json()["data"]["token"]
    write_file("./conf/user_token.txt",token)


def test_02_login_filed():
    #request请求代码
    url=d[1][2]
    data=eval(d[1][4])
    res = requests.post(url=url,json=data)

    assert res.status_code ==d[1][6]
    assert res.json()["status"]==d[1][7]
        #sql验证
    sql="select * from tb_user where username='{}' and password = '{}'".format(data['username'],data['password'])
    assert len(query(sql)) ==0
    