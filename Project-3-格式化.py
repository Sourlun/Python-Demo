# 位置参数 1
str = "{0} love {1}.{2}".format("I", "you", "yyy")
print(str)

# 位置参数 2
str = "{a} love {b}.{c}".format(a="I", b="you", c="yyy")
print(str)

# 位置参数 3 转换
str = "%c, %d, %c" % (97, 98, 99)
print(str)
