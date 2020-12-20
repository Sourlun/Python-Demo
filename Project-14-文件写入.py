import math

# 写入文件要以'w'模式
file = open('./file/writeFile.txt', 'w')

list = []
for item in range(1, 100):
    temp = math.pow(2, item)
    list.append(temp)

print(list)
练习
for item in list:
    file.write(str(item) + "\n")

# 最后写完需要关掉
file.close()
