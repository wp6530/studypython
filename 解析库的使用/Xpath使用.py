import requests
from lxml import html
etree = html.etree
# python3.5起，无法直接使用etree
text = '''
<div>
<ul>
<li class="item-0><a href="link1.html>first item</a></li>
<li class="item-1><a href="link2.html>second item</a></li>
<li class="item-inactive><a href="lin31.html>third item</a></li>
<li class="item-1><a href="link1.html>fourth item</a></li>
<li class="item-0><a href="link1.html>fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
# etree 模块可以自动补全
result = etree.tostring(html)
# print(result.decode('utf-8'))


# 直接读取文件进行解析
html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
# print(result.decode('utf-8'))

result_all = html.xpath('//*')
# print(result_all)
# *代表所有的节点
result_li = html.xpath('//li')
# print(result_li)
# 选取所有的li节点


# 子节点
# 可以通过/或//即可查找元素的子节点或子孙节点。如果想选择li节点的所有直接a子节点，可以使用//li/a实现
# 也可以使用//ul//a实现
result_li_a = html.xpath('//li/a')
# print(result_li_a)

# 不可以用//ul/a实现，ul节点没有直接的a子节点
result_lu_a = html.xpath('//lu/a')
# print(result_lu_a)

# 父节点
result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result)

# 属性匹配
result = html.xpath('//li[@class="item-0"]')
# print(result)

# 文本获取
result_a = html.xpath('//li[@class="item-0"]/a/text()')
result = html.xpath('//li[@class="item-0"]//text()')
# print(result_a)
# print(result)

# 属性获取
result = html.xpath('//li/a/@href')
# print(result)

# 属性多值匹配
text = '''
<li class ="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
# print(result)

# 多属性匹配
text = '''
<li class ="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
# print(result)


# 按序选择
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[1]/a/text()')
# print(result)
result = html.xpath('//li[last()]/a/text()')
# print(result)
result = html.xpath('//li[position()<3]/a/text()')
# print(result)
result = html.xpath('//li[last()-2]/a/text()')
# print(result)

# 节点轴选择
html = etree.parse('./test.html', etree.HTMLParser())

result = html.xpath('//li[1]/ancestor::*')
# 第一个li节点的所有祖先节点
result = html.xpath('//li[1]/ancestor::div')
# 第一个li节点的div祖先节点
result = html.xpath('//li[1]/attribute::*')
# attribute获取属性
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
# 选取href属性为link1.html的子节点
result = html.xpath('//li[1]/descendant::span')
print(result)





# 详细使用参考 www.w3school.com.cn/xpath/xpath_functions.asp
