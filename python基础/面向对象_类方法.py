class people:
    name = ''
    age = 0
    __weght =0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weght = w
        # __定义私有属性，私有属性在外部无法访问
    def speak(self):
        print("%s 说：我%d岁。" %(self.name, self.age))
p = people('wangpeng', 23, 75)
p.speak()


# 继承（单继承）
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade = g
    def speak(self):
        print("%s 说： 我%d岁，在读%d年级"%(self.name,self.age,self.grade))

s = student('ken', 10, 60, 3)
s.speak()


# 多继承


class speaker():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))



class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample("Tim", 23, 70, 3,"love")
test.speak()













