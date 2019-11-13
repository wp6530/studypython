import json

# 读取json
str = ''' [{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
},{
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
# }]'''
# print(type(str))
# data = json.loads(str)
# print(data)
# print(data[0]['name'])
# print(data[0].get('name'))
# print(data[0].get('age', 25))

# with open('data.json', 'r') as file:
#     str = file.read()
#     data = json.loads(str)
#     print(data)
# 输出json

with open('data_input.json', 'w') as file:
    # file.write(json.dumps(str))
    file.write(json.dumps(str, indent=5))