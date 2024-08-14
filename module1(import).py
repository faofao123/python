"""
#模块
一个.py文件就是一个模块,模块中可以定义变量、函数、类。
模块命名全部使用小写字母，多个单词之间使用下划线间隔。
重名时，优先导入自定义模块；默认后导入的。

#模块的导入
1.import 模块名称 [as 别名]
2.from 模块名称 import 变量/函数/类/*      *表示所有
"""
import module_a
module_a.info('fyz')

from module_a import info
info('FYZ')

import module_b   #此时程序输出模块b中的全局变量
                  #而模块a中使用了主程序运行规则（if __name__ == '__main__'）