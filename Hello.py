print("hello world!")

import sys
sys.setrecursionlimit(100000)
def fun(x):
    print(x*2)
    q = fun(x*2)
    return q
fun(2)