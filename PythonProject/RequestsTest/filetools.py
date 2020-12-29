def write_file(filepath, content):
    """
        文件写入方法
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(content)      # 写入内容


def read_file(filepath):
    """
        文件读取方法
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        res = f.read()            # read读取内容
    
    return res


if __name__ == "__main__":
    write_file("./123.txt", "请不要搞白,张家乐！")
    
    a = read_file("./123.txt")
    print(a)
