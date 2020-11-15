def fun(x, y, z):
    if(z < 0):
        return 0
    elif(z <= 2):
        return x + y
    else:
        return fun(y, x+y, z-1)

print(fun(0,1,100))


# 方法2
def fun2(n):
    if (n < 1):
        return 0
    elif (n <= 2):
        return 1
    else:
        return fun2(n-1) + fun2(n-2)

print(fun2(10))

