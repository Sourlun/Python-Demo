import urllib.request as req

response = req.urlopen('https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2943658165,3193430516&fm=26&gp=0.jpg')
image = response.read()

# with 打开文件后会自动关闭
with open('image/cat.jpg', 'wb') as f:
    f.write(image)

print(response.info())
print(response.getcode())