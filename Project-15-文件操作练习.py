import re


# 判断是否是数字
def is_number(num):
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = pattern.match(num)
    if result:
        return True
    else:
        return False


# 源文件
sourceFile = open('exercise/文件内容分类整理/文件内容分类整理.txt', encoding='UTF-8')
sourceList = list(sourceFile)
sourceFile.close()

# 存储数字的文件
numFile = open('exercise/文件内容分类整理/数字.txt', 'w', encoding='UTF-8')
# 存储不是数字的文件
strFile = open('exercise/文件内容分类整理/字符.txt', 'w', encoding='UTF-8')

for line in sourceList:
    if (is_number(line[0:1])):
        numFile.writelines(line)
    else:
        strFile.writelines(line)

print(sourceList)
numFile.close()
strFile.close()
