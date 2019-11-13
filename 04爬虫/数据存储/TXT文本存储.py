import  requests
from pyquery import PyQuery as pq
url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3933.0 Safari/537.36'
}
html = requests.get(url,headers=headers).text
print(html)
file = open('explore.txt', 'a', encoding='utf-8')
file.write(html)
file.close()