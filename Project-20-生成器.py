def myGen():
    print('生成器被执行')
    yield 1 # 第一次执行返回这个
    yield 2 # 第二次执行返回这个

myG = myGen()

print(next(myG))

print(next(myG))

# 循环输出
for item in myGen():
    print(item)


# 利用生成器做 斐波那契数列
print('---------- 斐波拉契数列--------------')
def libs():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a

for item in libs():
    if ( item > 1000 ):
        break
    print(item)


# --------- 列表推导式 --------------
print('--------- 列表推导式 --------------')
## 能被2整除 & 不能被3整除  ( i % 2 ) == 0, python当成false, 所以要在前面加not
listA = [i for i in range(1000) if not(i % 2) and (i % 3) ]
print(listA)


# ------------字典推导式 -------------------
print('------------字典推导式 -------------------')
## 被3整除就true, 否则false
dictA = { i:( i % 3 == 0 ) for i in range(1000)}
print(dictA)


# ------------- 累加推导式 --------------
print('------------- 累加推导式 --------------')
## 累加: 不能被2整除的数
sum1 = sum(  i for i in range(0,100) if(i%2) )
print(sum1)