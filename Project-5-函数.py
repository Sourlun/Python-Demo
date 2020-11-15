#  收集参数
def fun1(*params):
    print('参数的长度是:', len(params))
    for item in params:
        print('第' + item + '参数是' + item)


fun1('11', '22', '33', '44')

# 函数内部修改全局变量
num = 5
numGlobal = 5

def fun2():
    num = 10
    global numGlobal
    numGlobal = 10
    print(num)
    print(numGlobal)

print(num)
print(numGlobal)
fun2()

# 内嵌函数
def funa():
    def funab():
        print('funab')
    funab()
    print('funa')
funa()
