import time as t


class MyTimer():
    # 开始计时
    def start(self):
        self.startTime = t.localtime()
        print('计时开始!')

    # 计时结束
    def stop(self):
        self.endTime = t.localtime()
        print('计时结束!')

    # 内部方法, 计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了" # 双引号是不变字符串
        for index in range(6):
            self.lasted.append(self.startTime[index] - self.endTime[index])
            self.prompt += str( self.lasted[index] )
        print(self.prompt)

