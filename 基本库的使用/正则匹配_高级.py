import re
html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
      经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">笔记本</a></li>
        <li data-view="5">
        <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
result_active = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)

if result_active:
    print(result_active.group())
    # print(result_active.group(1), result_active.group(2))
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
if result:
    print(result.group())
    # print(result.group(1),result.group(2))
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
result_findall = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
for result in result_findall:
    # print(result)
    print(result[0], result[1], result[2])

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
content_sub = 'k1j1a4a1ad13sd5d1asd2a4adhksf'
content_sub = re.sub('\d+', '', content_sub)
print(content_sub)
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
html = re.sub('<a.*?>|</a>', '', html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
print(results)

for result in results:
    print(result.strip())

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'

pattern = re.compile('\d{2}:\d{2}')
results1 = re.sub(pattern, '', content1)
results2 = re.sub(pattern, '', content2)
results3 = re.sub(pattern, '', content3)
print(results1)
print(results2)
print(results3)




