score = int(input("请输入一个数字:"))
if 100 >= score:
    print("A+")
elif 90 <= score < 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif score < 80:
    print("不合格!")