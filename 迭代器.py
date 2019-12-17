#迭代器

a = [10,20,30]
y = iter(a) #创建一个迭代器
try:
    print(next(y))
    print(next(y))
    print(next(y))
    print(next(y))
except StopIteration:
    print("Error...")



#迭代对象
class A:
    def __init__(self):
        self.x = 0
    def __next__(self):
        self.x += 1
        if self.x > 10:
            raise StopIteration
        return self.x

    def __iter__(self):
        return self

a = A()
#print(set(a))
#print(list(a))

for i in a:
    print(i)