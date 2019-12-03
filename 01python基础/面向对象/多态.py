# -*-coding=utf-8-*-
class Person:
    def __init__(self, name):
        self.name = name

    def feed_pet(self, pet):
        if isinstance(pet, Pet):
            print('{} like {}({})'.format(self.name, pet.role, pet.nickname))
        else:
            print('NO!')


class Pet:
    role = 'Pet'

    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def show(self):
        print('nickname:{},age:{}'.format(self.nickname, self.age))


class Cat(Pet):
    role = 'cat'

    def catch_mouse(self):
        print('catch mouse')


class Dog(Pet):
    role = 'dog'

    def watch_door(self):
        print('watch door')


class Tigger:
    role = 'tigger'

    def eat_people(self):
        print('eat people')


cat = Cat('tom', 1)
dog = Dog('bob', 2)
tigger = Tigger()

person = Person('jack')
person.feed_pet(cat)

person = Person('jerry')
person.feed_pet(tigger)
person.feed_pet(dog)
