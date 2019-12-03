# -*-coding=utf-8-*-
# 使用模块变量
# 使用模块类
import mymode

num_list = [1, 2, 3, 4, 5, 6]
result = mymode.add(*num_list)
print(result)

'''
导入模块的方式：
1.import 模块名
    模块名.变量 模块名.函数 模块名.类 
2.from 模块名 import 变量|函数|类
    在代码中直接使用变量，函数，类
3.from 模块名 import *
4.无论是import还是from形式，都会将模块内容进行加载
如果不希望其进行调用，就会用到__name__
在自己的模块里面__name__叫：__main__
如果在其他模块中通过导入的方式调用的话：__name__:模块名

'''