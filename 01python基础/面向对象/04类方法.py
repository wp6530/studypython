# -*- coding:utf-8 -*-

'''
特点：
1. 定义需要依赖装饰器@classmethod
2. 类方法的参数不是一个对象，而是当前的类
3. 类方法中只可以访问类属性
4. 类方法中不能使用普通方法

作用：
因为只能访问类属性和类方法，在对象创建之前完成一些动作（功能）
'''


class Dog:
    nickname = 'jack'

    def __init__(self, nickname):
        self.nickname = nickname

    def run(self):
        print('{}在院子跑来跑去！'.format(self.nickname))

    # 类中方法的调用，需要使用self.方法名()
    def eat(self):
        print("吃饭。。。")
        self.run()

    @classmethod
    def test(cls):
        print(cls)
        print(cls.nickname)


# 类方法可以直接调用
# Dog.test()

d = Dog('danghuang')

d.run()
d.test()

d.eat()


class Person:
    __age = 18

    def show(self):
        print('----------->', Person.age)

    @classmethod
    def update_age(cls):
        cls.__age = cls.__age + 2

    @classmethod
    def show_age(cls):
        print("修改后的年龄是：", cls.__age)


# Person.age = Person.age + 1
Person.update_age()
Person.show_age()

p = Person()
# p.age = p.age + 1
# 操作的是对象的age，不会影响到类的age