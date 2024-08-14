"""
#包中模块的导入（__init__.py自动执行，但只执行一次）
1. import 包名.模块名 as 别名
2. from 包名 import 模块名 as 别名
3. from 包名.模块名 import 变量/函数/类/*

"""
import package.p_module as p_module
p_module.info()

from package import p_module
p_module.info()

from package.p_module import info
info()

from package.p_module import *
print(name)