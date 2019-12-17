# 魔术方法实例


'''
# __del__()析构方法

class File:
    def __init__(self,name):
        self.name = name
        print("open file",self.name)
    
    #read
    #
    #write
    
    def __del__(self):
        print("close file",self.name)

f1 = File("a.txt")

f2 = File("b.txt")

f3 = File("c.txt")

del f3
print("read...write...")
'''


'''
class Stu:
    name = "zhangsan"
    age = 20

    def __str__(self):
        return "name:%s;age:%d"%(self.name,self.age)

s = Stu()
print(s)
'''

'''
#__add__()

class Demo:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Demo(%d,%d)"%(self.x,self.y)

    def __add__(self,other):
        return Demo(self.x + other.x,self.y + other.y)

d1 = Demo(5,8)

d2 = Demo(9,-4)

print(d1 + d2)
'''


'''
class Rectangle:
    def __init__(self):
        self.width = 0
        self.heigth = 0

    def setSize(self,size):
        self.width, self.heigth = size

    def getSize(self):
        return self.width, self.heigth

    size = property(getSize, setSize)

r = Rectangle()
# r.width = 100
# r.heigth = 50
r.setSize((200,100))
print(r.getSize())

r.size = 1000, 500
print(r.size)
'''


"""
#静态方法和类成员方法

class A:
    '''使用装饰器定义静态和类成员方法'''
    @staticmethod   #静态方法定义
    def fun():
        print("aaaaaaaaaaaa..........")
    
    @classmethod    #类成员方法定义
    def demo(self):
        print("bbbbbbbbbbbb..........")
    
#a = A()
A.fun()
A.demo()
"""


class B:
    name = "zhangsan"
    __age = 20

    def fun1(self):
        print("aaa")

    def __dd(self):
        print("ccc")

b = B()
print(hasattr(b,"name"))
print(hasattr(b,"__age"))
print(hasattr(b,"fun1"))
print(hasattr(b,"__dd"))
