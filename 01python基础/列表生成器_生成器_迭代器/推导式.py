# -*- coding:utf-8 -*-
# 列表推导式
# 格式： [ 表达式 for 变量 in 旧列表 ] 或者[表达式 for 变量 in 旧列表 if 条件]
names = ['tom', 'jack', 'jerry', 'bob']
# 过滤掉长度小于或等于3的人名
result = [name for name in names if len(name) > 3]
print(result)

'''
def func(names):
    newlist=[]
    for name in names:
        if len(name)>3:
            newlist.append(name)
    return newlist  
'''

result = [name.capitalize() for name in names if len(name) > 3]
print(result)

newlist = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(newlist)

# def func():
#     newlist=[]
#     for i in range(5):
#         if i%2 == 0:
#             for j in range(5):
#                 if j%2 != 0:
#                     newlist.append((i , j))
#     print(newlist)
# func()

newlist = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 != 0]
print(newlist)

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
newlist = [i[-1] for i in list1]
print(newlist)

dict1 = {'name': 'tom', 'salary': 6000}
dict2 = {'name': 'jack', 'salary': 8000}
dict3 = {'name': 'bob', 'salary': 4500}
dict4 = {'name': 'jerry', 'salary': 3000}
dict5 = {'name': 'justin', 'salary': 5000}

list1 = [dict1, dict2, dict3, dict4, dict5]

newlist = [employee['salary'] + 200 if employee['salary'] > 5000 else employee['salary'] + 500 for employee in list1]

print(newlist)

# 集合推导式
# 在列表推导式的基础上增加了一个去除重复项的功能
list1 = [1, 2, 3, 4, 2, 1]
result = {x + 1 for x in list1}
print(result)

# 字典推导式
dict1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'C'}
newdict = {value: key for key, value in dict1.items()}
print(newdict)








