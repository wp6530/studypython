
class Myclass:
    '''这是一个简单的类实例'''
    i = 12345
    def f(self):
        return 'hello world'


# 实例化类
x = Myclass()

# print("Myclass 类的属性为：", x.i)
# print("Myclass 类的方法f输出为：", x.f())


# 类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

# self 代表类的实例，而非类


class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t = Test()
t.prt()

# self 代表的是类的实例，代表当前对象的地址，而self.class 指向类






















