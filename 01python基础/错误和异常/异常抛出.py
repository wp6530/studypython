# -*- coding:utf-8 -*-
def register():
    username = input('输入用户名：')
    if len(username) < 6:
        raise Exception('用户长度必须6位以上')
    else:
        print("输入的用户名是： ", username)


try:
    register()
except Exception as err:
    print("error: ", err)
    print("注册失败")
else:
    print("注册成功")


