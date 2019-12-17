# python的异常处理

print("Start...")

try:
    a = int(input("请输入一个数值："))
    print("你输入的值：",a)
    print(100/a)
except (ValueError,ZeroDivisionError) as info:
    print("错误！原因：",info)
    raise
except:
    print("未知错误!")

print("End...")
