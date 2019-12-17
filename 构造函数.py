# 构造函数：__init__()

'''
class A:
    def __init__(self):
        print("AAAAA")

    
    def fun(self):
        print("class A...")

a = A()
'''

class Person:
#    name = ""
#    age = 0
    def __init__(self,name,age):
        self.name = name
        self.__age = age#私有属性不可访问

    def getInfo(self):
        print(self.name,":",self.__age)
        self.__demo()

    def __demo(self):
        print("private method()")

p = Person("lisi",20)
print(p.name)
p.getInfo()
