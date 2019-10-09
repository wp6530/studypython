import requests
r = requests.get('https://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# # print(r.text)
# print(r.cookies)


r_get = requests.get('http://www.baidu.com/post')
r_put = requests.get('http://httpbin.org/put')
r_delete = requests.get('http://httpbin.org/delete')
r_head = requests.get('http://httpbin.org/head')
r_options = requests.get('http://httpbin.org/options')

print(r_get.text)
# print(r_put.status_code)
# print(r_delete.status_code)
# print(r_head.status_code)
# print(r_options.status_code)
