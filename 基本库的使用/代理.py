from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_hander = ProxyHandler({
    'http': 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=320000&city=321100&yys=0&port=1&pack=65978&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=',
    'https': 'https://127.0.0.1:9743'
})
opener = build_opener(proxy_hander)
try:
    response = opener.open('http://baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
