import json
data = {
    'no': 1,
    'name': 'Runoob',
    'url':  'http://www.runoob.com'
}

json_str = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)