import pymysql

def query(sql):
    """
        方法：查询数据库
        作用：传入sql语句，得到对应的结果
        参数：sql: 'select * from tb_user'
        返回值：((1,liuyun1, a12345678...), (2,liuyun2, a123456,...))
    """
    # 连接数据库
    db=pymysql.connect(host='118.24.255.132', user='testgoup', password='1qaz!QAZ', db='taskDB')

    # 获取查询窗口：游标
    cur = db.cursor()
    # 执行sql
    cur.execute(sql)
    # 获取所有的结果
    res = cur.fetchall()
    # 关闭数据库连接
    db.close()
    return res


# 为了防止其他的py文件导入这个文件时运行调试代码
# 主要时为了测试方法是否有问题
if __name__ == "__main__":
    sql = "select * from tb_user where password=123456"
    r = query(sql)
    print(len(r)) 