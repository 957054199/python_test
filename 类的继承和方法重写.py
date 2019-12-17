# 类的继承和方法重写

class Person:#基类
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getInfo(self):
        print("我的名字：%s；年龄：%d岁。"%(self.name,self.age))

class Stu(Person):#派生类
    def __init__(self,name,age,school):
        Person.__init__(self,name,age)
        self.school = school

    def getInfo(self):
        print("我的名字：%s；年龄：%d岁；学校：%s。"%(self.name,self.age,self.school))

    def fun(self):
        print("hello world")

s = Stu("zhangsan",20,"北京大学")
s.getInfo()
s.fun()
