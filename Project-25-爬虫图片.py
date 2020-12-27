import urllib.request
import os
import base64

#
#   打开url
#
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

#
#   获取当前页面是位于多少页
#
def get_page(url):
  html = url_open(url).decode('utf-8')

  # 页数的起始坐标
  start = html.find('current-comment-page') + 23
  # 页数的结束坐标
  end = html.find(']', start)

  # print(html)
  page_num = html[start:end]
  print(page_num)
  return page_num

#
# 根据url找到该url下的图片地址, 返回list
#
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    start = html.find('img src=')

    while True:
        end = html.find('.jpg', start, start + 100)  # 第三个参数: 大于某个值就不找了
        if end != -1:
            img_addr = html[start + 11:end + 4]
            img_addr = 'http://' + img_addr
            img_addrs.append(img_addr)
        else:
            end = start + 10
        start = html.find('img src=', end)
        if start == -1:
            break
    print(img_addrs)
    return img_addrs

#
#   根据图片url地址保存图片
#
def save_images(folder, image_addr):
    for each in image_addr:
        file_name = each.split('/')[-1] # 获得一个url最后一个/后的字符串
        with open(file_name, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download_img(folder = 'image/爬图片', pages = 10):
    # os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx'
    page_num = int( get_page(url) )


    for i in range(pages):
        current_page_num = page_num - i
        a = str('20201227-') + str(current_page_num)
        commons = base64.b64encode( a.encode('utf-8') ) # 需要转成2进制格式才可以转换，所以我们这里再手动转换一下
        page_url = url + '/' + str(commons, 'utf-8') + '#comments'
        print(page_url)
        # 查询该网页上的图片地址
        image_url = find_imgs(page_url)
        save_images(folder='', image_addr=image_url)


if __name__ == '__main__':
    download_img()