def fun(n, a, b, c):
    if(n <= 1):
        print(a + '----------->' + c)
        return
    fun(n-1, a, c, b)
    print(a + '------------->' + c)
    fun(n-1, b, a, c)

fun(3, 'a', 'b', 'c')