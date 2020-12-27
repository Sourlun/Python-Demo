import urllib.response
import urllib.request

 # 查询当前请求的ip地址
url = 'http://ip.webmasterhome.cn/'

 # 代理的ip
ip = '58.253.156.14:9999'
 # 设置代理的ip
proxy_support = urllib.request.ProxyHandler({'http': ip})

opener = urllib.request.build_opener(proxy_support)
 # 添加代理请求的headser
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')
print(html)


