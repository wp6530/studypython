
class Computer:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def online(self):
        print("正在使用电脑上网...")

    def __str__(self):
        return self.brand + '---' + self.color


class Book:
    def __init__(self, bname, author, number):
        self.bname = bname
        self.author = author
        self.number = number

    def __str__(self):
        return self.bname + '---' + self.author + '---' + str(self.number)


class Student:
    def __init__(self, name, computer, book):
        self.name = name
        self.computer = computer
        self.books = []
        self.books.append(book)

    def borrow_book(self, book_new):
        for book in self.books:
            if book.bname == book_new.bname:
                print("已经借过了")
                break
        else:
            self.books.append(book_new)
            print("添加成功")

    def show_book(self):
        for book in self.books:
            print(book.bname)

    def __str__(self):
        return self.name + '---' + str(self.computer) + '---' + str(self.books)


# 创建对象
computer = Computer('mac pro 2018', '深灰色')
book1 = Book('盗墓笔记', '南派三叔', 10)
book2 = Book('鬼吹灯', '霸唱天下', 8)

stu = Student('jack', computer, book1)
print(stu)

stu.borrow_book(book2)
stu.show_book()
