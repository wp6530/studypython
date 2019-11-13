# -*- coding:utf-8 -*-

# try:
#     s = None
#     if s is None:
#         print("s 是空对象")
#         raise NameError
#     print(len(s))
# except TypeError:
#     print("空对象没有长度")
#
# s = None
# if s is None:
#     raise NameError
# print("is here")

class PasswordException(Exception):
    def __init__(self, password):
        self.password = password
    def __str__(self):
        return repr(self.password)

def testraise():
    try:
        username = input("please input your username:")
        if username !="admin":
            raise Exception(f"maybe your privilege is not enough: {username}")
    except Exception as e:
        print(f"{e}")
    try:
        password = input("please enter your password:")
        if password != "123456":
            raise PasswordException(password)
    except PasswordException as e:
        print(f"PasswordException: {e.password}")

if __name__ == "__main__":
    testraise()