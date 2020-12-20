import pickle

list = [123, 234, '2gf', '十大高手', [234, '234234', '山豆根山豆根是']]

# 'wb'二进制的写入形式
listPickleFile = open('./file/list_pickle.txt', 'wb')

# 把 list 的内容序列号放到 listPickleFile 里面
pickle.dump(list, listPickleFile)

listPickleFile.close()

# 'rb' 以二进制形式读取
listPickleFile = open('./file/list_pickle.txt', 'rb')
# 以二进制的形式加载文件
list = pickle.load(listPickleFile)
print(list)
