# 创建元组
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d", "d"
print(type(tup3))

# 访问元组
print(tup1[0])
print("tup2[1:5]:", tup2[1:5])


# 修改元组
# # 元组中的元素值不允许修改，但我们可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print(tup3)

# # 可以通过列表组成元组进行修改
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
tup3 = (list1, list2)
list2[1] = 9

# # 删除后输出有问题 NameError: name 'tup3' is not defined
print(tup3)
del tup3
print(tup3)

# 元组索引




