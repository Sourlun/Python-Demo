# 批量对应
dic1 = {}
dic1 = dic1.fromkeys((1, 2, 3))
print(dic1)


dic2 = {}
dic2 = dic2.fromkeys((1, 2, 3), "value")
print(dic2)

dic3 = {}
dic3 = dic3.fromkeys((1, 2, 3), ("v1", "v2", "v3"))
print(dic3)

# 打印
dic4 = {}
dic4 = dic4.fromkeys(range(0, 10), '我要好运')
for key in dic4:
    print(dic4[key])
for item in dic4.keys():
    print(item)
for item in dic4.items():
    print(item)
# 获取一个不存在的项,并不会报异常
print(dic4.get(21))
# 判断某个项是否在字典里
print(10 in dic4)
# 清空字典
dic4.clear()
print(dic4)