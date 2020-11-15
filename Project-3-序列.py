# 字符串转list
a = "进入修改python的页面后，就可以修改所有类型的字体了，如下图"
a = list(a)
print(a)
# 长度
print(len(a))
# 最大值
print(max(a))

num = (45,78,45,36,87,44,1,2,55,96,55,74,-85)
# 求和
print(sum(num))
# 排序
print(sorted(num))
# 排序 (倒序)
print(list(reversed(num)))
# 变成枚举后转成list
print(list(enumerate(num)))