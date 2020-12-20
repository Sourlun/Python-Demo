import urllib.request as req
import urllib.parse as par
import json

# 翻译的请求地址
transationUrl = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
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

# 编码格式转换
data = par.urlencode(data)
# encode:是转码从unicode转成xx码
data = data.encode('utf-8')


response = req.urlopen(transationUrl, data)
# decode: 是解码从xx字符转成unicode
html = response.read().decode('utf-8')
print(html)

# json字符串 转 字典
map = json.loads(html)
print(map)
print('翻译后的结果:' + map['translateResult'][0][0]['tgt'])