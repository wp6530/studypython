import re
print('+++++++++++++++content1+++++++++++++++++++++')
content1 = 'Hello 1234567 World_This is a Regex Demo'
result1 = re.match('^Hello\s(\d+)\sWorld', content1)
greed = re.match('^He.*(\d+).*Demo$', content1)
ungreed = re.match('^He.*?(\d+).*Demo$', content1)
# print(result1)
# print(result1.group())
# print(result1.group(1))
# print(result1.span())
print('贪婪：', greed.group(1))
print('非贪婪：', ungreed.group(1))

print('+++++++++++++++content2+++++++++++++++++++++')
content2 = 'Hello 123 4567  World_This is a Regex Demo'
result2 = re.match('^Hello(.*)Demo$',content2)
print(result2)
print(result2.group())
print(result2.group(1))
print(result2.span())


print('+++++++++++++++content3_修饰符+++++++++++++++++++++')
content3 = '''Hello 1234567 World_This 
is a Regex Demo
'''
result3 = re.match('^He.*?(\d+).*Demo$', content3,re.S)
print(result3.group(1))
# .匹配的是非换行符的所有字符，加上re.S可以匹配所有字符

print('+++++++++++++++content3_转义符+++++++++++++++++++++')
content4 = '(百度)www.baidu.com'
result4 = re.match('^\(百度\).*',content4)
print(result4)
print(result4.group())
print(result2.span())