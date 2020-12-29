import pytest
import requests

import os,sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import read_file
from utils.filetools import write_file
from utils.exceltools import read_excel

#数据和脚本分离出来，d放到外面作为公用变量
d= read_excel('data/datas.xlsx',"首页")

def test_03_banalist():
    '''获取首页轮播图'''
    url=d[0][2]
    header=eval(d[0][5])
    res = requests.get(url=url,headers=header)
    print(res.text)
    assert res.status_code ==200
    assert res.json()["status"]==200


    #for循环遍历数组来查询sql
    data=res.json()["data"]
    for i in data:
        imghost=d['imghost']
        linkurl=d['linkurl']
        sql="select * from tb_system_banner where imghost='{}' and linkurl='{}'".format(imghost,linkurl)
        assert len(query(sql))!=0
