# -*- coding:utf-8 -*-
# 异常处理
'''
try:
    可能出现异常的代码
except:
    如果有异常执行的代码
[finally:
    无论是否存在异常都会执行的代码]

情况1：
try:
    有可能产生多种异常
except 异常的类型1:
    print("xxxxxxxx")
except 异常的类型2：
    print("xxxxxxxx")
except Exception as err:
    print("error: ", err)

try:
    pass
except :
    pass
finally:
    pass

'''


def func():
    try:
        n1 = int(input("输入第一个数字： "))
        n2 = int(input("输入第二个数字： "))
        per = input("输入运算符号：( + — * /): ")
        result = 0
        if per == '+':
            result = n1 + n2
        if per == '-':
            result = n1 - n2
        if per == '*':
            result = n1 * n2
        if per == '/':
            result = n1 / n2
        else:
            print("符号输入错误")
        print("reslut  = ", result)
    # except ZeroDivisionError:
    #     print("除数不能为0")
    # except ValueError:
    #     print("输入不为数字")
    except Exception as err:
        print("error: ", err)


# func()

def file():
    stream = None
    try:
        stream = open('test.txt')
        container = stream.read()
        print(container)
    except Exception as err:
        print(err)
    finally:
        print("close file")
        if stream:
            stream.close()


file()
