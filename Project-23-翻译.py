import urllib.request as req
import urllib.parse as par
import json

# 1, 翻译的请求地址
transationUrl = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

# 2, 设置请求数据, header
# 要翻译的内容
needTransStr = '第一个程序化翻译'
data = {
    'i': needTransStr,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '16084573396238',
    'sign': '46f53908e46388d6dbceb5336770297f',
    'lts': '1608457339623',
    'bv': 'e352c26cfcd0c5f4e08ab85e750e759a',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'
}

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'

# 编码格式转换
data = par.urlencode(data)
# encode:是转码从unicode转成xx码
data = data.encode('utf-8')

 # 设置request请求
request = req.Request(transationUrl, data, headers)
 # 两种方式添加header
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66')

 # 3, 请求接口
response = req.urlopen(request)

 # 4, 读取返回的数据
# decode: 是解码从xx字符转成unicode
html = response.read().decode('utf-8')
print(html)

# json字符串 转 字典
map = json.loads(html)
print(map)
print('翻译后的结果:' + map['translateResult'][0][0]['tgt'])