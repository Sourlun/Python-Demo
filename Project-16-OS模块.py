import os

# 当前路径
cwd = os.getcwd()
print('当前目录' + cwd)

# 切换路径
os.chdir('D:\\')
print('改变后的路径: ' + os.getcwd())

# 列举当前的文件
print(os.listdir(os.getcwd()))

# 运行SHELL命令
os.system('ipconfig')

