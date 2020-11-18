# 默认是只读的方式
file = open("file/text.txt")
print(file)

# 关闭文件
file.close()

# 以UTF-8的方式打开， 不然打不开
file = open("file/text.txt", encoding='utf-8')

# 读文件
str = file.read()
print(str)
print('-----------------读文件完成-------------------')

# 读取前 x 个字符
str = file.read(20)
print(str)

# 当前文件 指针 的位置
str = file.tell()
print(str)

# 移动 指针 的位置  参数一：偏移多少个字节；  参数二：（0：起始位置； 1：当前位置； 2：文件末尾）
file.seek(100, 0)
print(file.tell())

print(" -----  移动 指针 的位置  参数一：偏移多少个字节；  参数二：（0：起始位置； 1：当前位置； 2：文件末尾）")

# 当前指针显示当前一行
str = file.readline()
print(str)


# 文件转列表 (按行分割）
file.seek(0,0)
list1 = list(file)
print(list1)