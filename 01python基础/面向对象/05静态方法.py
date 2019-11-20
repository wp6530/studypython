# -*- coding:utf-8 -*-
'''
静态方法：
1. 需要装饰器@staticmethod
2. 静态方法无需传递参数
3. 只能访问类的属性和方法
4. 加载的时机和类方法一样

总结：
类方法和静态方法

不同：
1. 装饰器不同
2. 类方法是有参数的，静态方法没有参数

相同：
1. 只能访问类的属性和方法，对象的是无法访问的
2. 都可以通过类名调用访问
3. 都可以在创建对象之前调用，因为都不依赖对象

普通方法与两者的区别：
1. 没有装饰器
2. 普通方法永远需要依赖对象，应为每个普通方法都需要有一个self
3. 只有创建了对象才能调用普通方法，否则无法调用



'''


class Person:
    __age = 20

    def __init__(self, name):
        self.name = name

    @staticmethod
    def test():
        print('---------->静态方法')
        # print(self.name)# 语法错误
        print(Person.__age)


p = Person('jack')
p.test()


