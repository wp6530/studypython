import requests
import re

# r = requests.get("http://httpbin.org/get")
# print(type(r.text))
# print(r.text)
# print(type(r.json()))
# print(r.json())
# 调用json()方法，将返回结果由字符串转化为字典
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3933.0 Safari/537.36'
}
# 添加headers信息，包含User-Agent字段信息，也就是浏览器表示信息。如果不加，知乎禁止抓取。

r = requests.get("https://www.zhihu.com/explore", headers=headers)
# r = requests.get("https://www.zhihu.com/explore")

# print(r.text)

# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
pattern = re.compile('data-za-detail-view-id=.*>(.*?)</a>',re.S)


# titles = re.findall(pattern, r.text)
# print(titles)
paper = requests.get("https://pic1.zhimg.com/80/v2-a413ab3d307d1a06ee07df24ebafca2e_hd.jpg")
# print(paper.text)
# print(r.content)

with open('v2-a413ab3d307d1a06ee07df24ebafca2e_hd.jpg','wb') as f:
    f.write(paper.content)
