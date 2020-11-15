# 过滤false的值
v1 = filter(None, [1, 8, 0, True, False, 33, -1])
print(list(v1))

# 过滤掉被3整除的数
def fun1(x):
    return x % 3 != 0
v2 = filter(fun1, range(-1000, 1000))
print(list(v2))

# 过滤不能被5整除的数
v3 = filter(lambda x: x % 5 == 0, range(0, 1000))
print(list(v3))

# 所有数*2
v4 = map(lambda x: x * 2, range(1, 1000))
print(list(v4))