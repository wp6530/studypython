from bs4 import BeautifulSoup
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="'link1"><!--Elsie--></a>,
    <a href="http://example.com/lacie" class="sister" id="'link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="'link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
<p class="story">...
</p>

'''
soup = BeautifulSoup(html, 'lxml')
# 使用 lxml 解析器对html进行BeautifulSoup初始化，补全html节点
# print(soup.prettify())
# 将要解析的字符串以标准的缩进格式输出
# print(soup.title.string)

# 节点选择器
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)

print(soup.p)
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p.string)


# 嵌套选择
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)
