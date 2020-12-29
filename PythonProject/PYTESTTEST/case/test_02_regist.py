#注册
#请用pytest的测试方法一下三个测试用例：自己手写
#1、已存在的账号注册失败
#2、账号长度不规范注册失败
#3、注册成功
import pytest,requests

def test_02_reg_failed1():
    '''
    1、已存在的账号注册失败
    '''
    url="http://zzy.testgoup.com/api/regist"
    data={"username":"liuyun1","password":"a12345678"}
    res=requests.post(url=url,json=data)
    assert res.status_code == 200
    assert res.json()["status"]==401

def test_02_reg_failed2():
    '''
    2、账号长度不规范注册失败
    '''
    url="http://zzy.testgoup.com/api/regist"
    data={"username":"","password":"a12345678"}
    res=requests.post(url=url,json=data)
    assert res.status_code == 200
    assert res.json()["status"]==401

def test_02_reg_failed3():
    '''
    3、注册成功
    '''
    url="http://zzy.testgoup.com/api/regist"
    data={"username":"liuyun367","password":"a12345678"}
    res=requests.post(url=url,json=data)
    assert res.status_code == 200
    assert res.json()["status"]==401
    