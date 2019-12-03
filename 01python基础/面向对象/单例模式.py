# -*- coding=utf-8 -*-
# 单例模式
# 开发模式

class Singleton:
    # 私有化，单例的地址就存放于此
    __instance = None

    # 重写__new__
    def __new__(cls):
        print('--->new')
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            # print(cls.__instance)
            return cls.__instance
        else:
            return cls.__instance


s = Singleton()
s1 = Singleton()
print(dir(Singleton))
print(s)
print(s1)
