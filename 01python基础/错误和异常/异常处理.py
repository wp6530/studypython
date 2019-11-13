# -*- coding:utf-8 -*-
# while True :
#     try:
#         x = int(input("please input a number:"))
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try again")
# 一个try语句可能包含多个except子句，一个except子句可以同时处理多个异常

import sys
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:{0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise


# param1 = sys.argv[1]
# param2 = sys.argv[2]
# param3 = sys.argv[3]
# param4 = sys.argv[4]
# param5 = sys.argv[5]


# print(param1, param2, param3, param4, param5)


# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

# 抛出异常
