#当前目录下

'''
import 模块导入
from 模块导入 import sum
print("100的累加：",模块导入.sum(100))
print("50的累加：",sum(50))
'''

#导入自定义的模块文件（mylib包）
from mylib import 模块导入
from mylib.模块导入 import sum
print("100的累加：",模块导入.sum(100))
print("50的累加：",sum(50))

print(模块导入.__name__)