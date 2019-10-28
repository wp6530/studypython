# -*- coding:utf-8 -*-
# 属性
# class Province:
#     # 类属性
#     country = '中国'
#
#     def __init__(self, name):
#         # 实例属性
#         self.name = name
#
#
# obj = Province('河南省')
# print(obj.name)
# print(Province.country)

# 实例属性属于对象，类属性属于类


# 方法

# 普通方法：由对象调用；至少一个self参数；执行普通方法时，自动将调用该方法的对象赋值给self；self是实例的变量名；(类不能调用实例的方法)

# 静态方法：由类调用；默认无参数，可以任意参数；(对象也能调用)

# 类方法：由类调用； 至少一个cls参数；执行类方法时，自动将调用该方法的类复制给cls；cls其实是类名，类方法其实是静态方法的一个变种；(对象也能调用)
#
# class Province:
#     country = "China"
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print(self.name)
#
#     def f1(arg1,arg2):
#         print(arg1,arg2)
#
#     def f2(cls):
#         print(cls)
#
#
# obj = Province('python')
# print(obj.name)
# obj.show()
#
# Province.f1(111, 222)
# Province.f2(obj)
#
# # obj.f1('python')
# obj.f2()


# 包装
class Foo:
    def func(self):
        pass
    @property
    def prop(self):
        print("将方法包装成属性访问即包装")
        return  123


# fool_obj = Foo()
# ret = fool_obj.prop
# print(ret)

class Paper:
    def __init__(self, current_page):
        self.current_page = current_page
        self.per_items = 10
    @property
    def start(self):
        val = (self.current_page -1) * self.per_items
        return  val
    @property
    def end(self):
        val = self.current_page * self.per_items
        return val

p = Paper(1)
print(p.start)
print(p.end)

# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。