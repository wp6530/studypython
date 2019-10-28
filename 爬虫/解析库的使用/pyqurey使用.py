from pyquery import PyQuery as pq
# 引入PyQuery这个对象，取别名为pq
import  requests
html = '''
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
doc = pq(html)
# print(doc('li'))
# print('+++++++++++++++++++++++++++++++++++++')
# print(doc)
# print('+++++++++++++++++++++++++++++++++++++')
# print(html)
# print('+++++++++++++++++++++++++++++++++++++')
# 初始化的参数不仅可以用字符串的形式传递，同样可以用html和本地文件的形式传递

# url初始化
doc = pq(url='https://cuiqingcai.com')

# print(doc('title'))

# 文件初始化
doc = pq(filename='test.html')
# print(doc)

# css选择器

doc = pq(html)
# print(doc)
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))


items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)