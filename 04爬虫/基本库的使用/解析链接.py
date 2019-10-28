from urllib.parse import urlparse
from urllib.parse import urlunparse

from urllib.parse import urlsplit
from urllib.parse import urlunsplit

result_urlparse = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
result_urlsplit = urlsplit('http://www.baidu.com/index.html;user?a=6#comment')

result_scheme = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
result_fragment = urlparse('https://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)

print('{}: {}'.format('result_urlparse', result_urlparse))
print('{}: {}'.format('result_urlsplit', result_urlsplit))
print('{}: {}'.format('result_scheme', result_scheme))
print('{}: {}'.format('result_fragment', result_fragment))

# print(result.scheme, result[0], result.netloc, result[1], sep = '\n')
# print(result.scheme,result[0])

# 拼接链接

data_unparse = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
data_unsplit = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']

print(urlunparse(data_unparse))
print(urlunsplit(data_unsplit))
