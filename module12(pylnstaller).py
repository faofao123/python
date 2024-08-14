"""
 第三方库Pyinstaller可以在Windows操作系统中将Python源文件打包成.exe的可执行文件。
 还可以在Linux和Mac OS操作系统中对源文件进行打包操作。

 打包的语法结构为：pyinstaller-F源文件文件名

 ***注意事项：
 在进行文件打包时，需要打包的文件尽量不要有中文，而且需要打包的文件路径也尽量不要有中文，路径中包含中文有可能会导致打包失败。
"""
#需要在终端操作
#例：pyinstaller -F D:\jetbrians\PycharmProjects\xuexi\print.py