# -*- coding:utf-8 -*-

# 方法
# 种类： 普通方法 类方法 静态方法 魔术方法

'''
普通方法格式：
def 方法名 (self[，参数，参数]):
'''


class Phone:
    brand = 'xiaomi'
    price = 4999
    type = 'mate X'
    # note = ''
    # address_book = []

    def call(self):
        print("address of self :", self)
        print("正在访问通讯录：")
        for person in self.address_book:
            print(person.items())
        print('正在打电话...')
        print("留言：", self.note)


phone1 = Phone()
print(phone1)
phone1.note = '我是phone1'
phone1.address_book = [{"1536613822": "jack"}, {"153641222": "tom"}]
phone1.call()

print('*' * 30)
phone2 = Phone()
print(phone2)
phone2.note = '我是phone2'
# phone2.address_book = [{"1536613822": "jack"}, {"153641222": "tom"}]
# phone2.call()
