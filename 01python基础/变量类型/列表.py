# 列表的数据项不需要具有相同的类型

# 创建列表
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

# 访问列表
print("list1[0]:", list1[0])
print("list2[1:5]:", list2[1:5])

# 更新列表
list1[1] = 'baidu'
print(list1)

# 删除列表
del list1[2]
print(list1)

# 函数和方法

print("list2元素个数：", len(list2))
print("list2最大值：", max(list2))
print("list2最小值：", min(list2))

print("list1+list2:", list1+list2)
print("list2[-2]:", list2[-2])
print("list2[1:]:", list1[1:])

list2.append(6)
print("list2:", list2)
print(list2.count(2))
print(list2.index(2))

list2.reverse()
print(list2)

