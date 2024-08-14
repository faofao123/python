"""
字符串的验证（不太重要）
str.isdigit()所有字符都是数字（阿拉伯数字）
str.isnumeric()所有字符都是数字
str.isalpha()所有字符都是字母（包含中文字符）
str.isalnum()所有字符都是数字或字母（包含中文字符）
str.islower()所有字符都是小写
str.isupper()所有字符都是大写
str.istitle()所有字符都是首字母大写(且只有首字母大写)
str.isspace()所有字符都是空白字符

"""
print('123'.isdigit())
print('helloworld'.islower())

"""
正则表达式和re模式（有点高级了，初学不建议碰）
元字符
1. .   匹配任意字符（除了\n）
2. \w  匹配字母、数字、下划线
3. \W  匹配非字母、数字、下划线
4. \s  匹配任意空白字符
5. \S  匹配任意非空白字符
6. \d  匹配任意十进制数
"""