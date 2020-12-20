import urllib.request as re

response = re.urlopen('https://baike.baidu.com/item/%E8%85%BE%E8%AE%AF')
# 以二进制打开
html = response.read()
print(html)
# 设置解码方式
html = html.decode("UTF-8")
print(html)


