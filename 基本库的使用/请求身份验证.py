from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError

username = 'wangpeng'
password = 'asdasd'
url = 'http://106.14.180.26/hello'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_hander = HTTPBasicAuthHandler(p)
opener = build_opener(auth_hander)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
