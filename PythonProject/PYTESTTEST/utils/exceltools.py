"""
    读取excel
"""
import xlrd

def read_excel(excel_path, sheet_name, skip_first=True):
    """
        方法名：读取excel
        参数：
            excel_path：excel的路径
            sheet_name：table页面的名字
            skip_first：是否跳过首行，默认为是
        返回值：[[1,2,3,4,], [1,2,3,4]]
    """
    results = []
    datas = xlrd.open_workbook(excel_path)
    table = datas.sheet_by_name(sheet_name)
    if skip_first == True:
        start_row = 1
    else:
        start_row = 0
    
    # 循环读取每一行的数据 (1,2)
    for row in range(start_row, table.nrows): # (1,2)
        results.append(table.row_values(row))

    return results

if __name__ == "__main__":
    data = read_excel('D:\\Awork\\ljtest202011\\PythonProject\\PYTESTTEST\\data\\datas.xlsx', "登录")
    print(data)

