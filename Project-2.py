str = "一款用于翻译的插件，包括谷歌翻译、有道翻译，妈妈再也不怕我不懂英文啦。"
for item in str:
    print(item, end=' ')

# 列表
strList = ["af", "fsdf", "isdfjs", "153", "ioehf", "3143540"]
for item in strList:
    print(item, len(item))

# 跳过 ( 从1到10, 两个两个来遍历 )
for i in range(1, 10, 2):
    print(i)

# 元组 (值不能改变)
tuple1 = (1,2,3,4,5,6,7,8,9,10)
for i in tuple1:
    print(i)