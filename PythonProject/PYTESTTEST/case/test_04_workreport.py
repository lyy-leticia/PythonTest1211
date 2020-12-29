import pytest
import requests

import os,sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import read_file
from utils.filetools import write_file
from utils.exceltools import read_excel

def test_04_workreport_success():
    '''
    1\换一个接口,不行都不知道哪儿错了
    '''
    url="https://lt.itsyw.cn/Pm/GetPm.ashx"
    data= {"action":"pm"}
    res=requests.get(url=url,json=data)
    print(res.text)
    assert res.status_code == 200
    assert res.json()["status"]==200