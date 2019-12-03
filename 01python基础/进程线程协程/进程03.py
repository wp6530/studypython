# -*- coding=utf-8 -*-
# from multiprocessing import Process
#
#
# class MyProcess(Process):
#     def __init__(self, name):
#         super(MyProcess, self).__init__()
#         self.name = name
#
#     # 重写run
#     def run(self):
#         n = 1
#         while True:
#             # print("the name of process: ", self.name)
#             print('{}------>自定义进程：n:{}'.format(n, self.name))
#             n += 1
#
#
# if __name__ == '__main__':
#     p1 = MyProcess('xiaoming')
#     p1.start()
#     p2 = MyProcess('xiaohong')
#     p2.start()

class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')
