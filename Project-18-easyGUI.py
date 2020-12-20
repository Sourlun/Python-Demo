import easygui as g

g.msgbox('Hello World')

# 选项窗口
if g.ccbox("亲爱的还玩吗?", choices=("还要玩！", "算了吧/(ㄒoㄒ)/~~")):
    g.msgbox("还是不玩了，快睡觉吧！")
else:
    g.msgbox("好吧")

# 按钮窗口
g.buttonbox(msg="你喜欢下面哪种水果?", title="", choices=("西瓜", "苹果", "草莓"))


g.buttonbox("大家说嗅嗅可爱吗?",image="./image/捕获2.PNG",choices=("可爱","不可爱","财迷"))