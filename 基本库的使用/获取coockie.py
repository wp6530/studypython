import http.cookiejar,urllib.request
# coockie = http.cookiejar.CookieJar()
# hander = urllib.request.HTTPCookieProcessor(coockie)
# opener = urllib.request.build_opener(hander)
# response = opener.open('http://www.baidu.com')
# for item in coockie:
#     print(item.name+"="+item.value)
# 生成文件
filename = 'coockies.txt'
coockie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(coockie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
coockie.save(ignore_expires=True)



