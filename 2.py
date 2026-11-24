# 这里是Python练习场,可以使用ctrl+/   一键注释和解除一键注释
# 来源:https://github.com/jackfrued/Python-100-Days

# print('Hello,World')

#  Hello,World

# print(0x100)
# print(0b100)
# print(0o100)
# print(100)
# print(123.456)
# print(123456e2)

# a = 11
# b = 45
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

"""
使用type函数检查变量的类型

"""
# a = 100
# b = 123.45
# c = 'hello, world'
# d = True
# print(type(a))  # <class 'int'>
# print(type(b))  # <class 'float'>
# print(type(c))  # <class 'str'>
# print(type(d))  # <class 'bool'>
"""
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串（在可能的情况下）转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码方式。
chr()：将整数（字符编码）转换成对应的（一个字符的）字符串。
ord()：将（一个字符的）字符串转换成对应的整数（字符编码）。
"""

"""
变量的类型转换操作
"""
# a = 100
# b = 123.45
# c = '123'
# d = '100'
# e = '123.45'
# f = 'hello, world'
# g = True
# print(float(a))         # int类型的100转成float，输出100.0
# print(int(b))           # float类型的123.45转成int，输出123
# print(int(c))           # str类型的'123'转成int，输出123
# print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
# print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
# print(float(e))         # str类型的'123.45'转成float，输出123.45
# print(bool(f))          # str类型的'hello, world'转成bool，输出True
# print(int(g))           # bool类型的True转成int，输出1
# print(chr(a))           # int类型的100转成str，输出'd'
# print(ord('d'))         # str类型的'd'转成int，输出100

"""
算术运算符

"""
# print(321 + 12)     # 加法运算，输出333
# print(321 - 12)     # 减法运算，输出309
# print(321 * 12)     # 乘法运算，输出3852
# print(321 / 12)     # 除法运算，输出26.75
# print(321 // 12)    # 整除运算，输出26
# print(321 % 12)     # 求模运算，输出9
# print(321 ** 12)    # 求幂运算，输出1196906950228928915420617322241
# print(2 ** 3)

"""
算术运算的优先级

"""
# print(2 + 3 * 5)           # 17
# print((2 + 3) * 5)         # 25
# print((2 + 3) * 5 ** 2)    # 125
# print(((2 + 3) * 5) ** 2)  # 625

"""
赋值运算符和复合赋值运算符

"""
# a = 10
# b = 3
# a += b        # 相当于：a = a + b
# a *= a + 2    # 相当于：a = a * (a + 2)
# print(a)      # 大家算一下这里会输出什么
# 1.a+b=10+3=13=a 2.a*(a+2)=13*(13+2)=195

"""
海象运算符

"""
# SyntaxError: invalid syntax
# print((a = 10))
# 海象运算符

# print((a := 10))  # 10
# print(a)          # 10

"""
比较运算符和逻辑运算符的使用

"""
# flag0 = 1 == 1
# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not flag0
# print('flag0 =', flag0)     # flag0 = True
# print('flag1 =', flag1)     # flag1 = True
# print('flag2 =', flag2)     # flag2 = False
# print('flag3 =', flag3)     # flag3 = False
# print('flag4 =', flag4)     # flag4 = True
# print('flag5 =', flag5)     # flag5 = False
# print(flag1 and not flag2)  # True
# print(1 > 2 or 2 == 3)      # False

# 说明：比较运算符的优先级高于赋值运算符，所以上面的flag0 = 1 == 1先做1 == 1产生布尔值True，
# 再将这个值赋值给变量flag0。print函数可以输出多个值，多个值之间可以用,进行分隔，输出的内容默认以空格分开。

# 例子1：华氏温度转摄氏温度
#　要求：输入华氏温度将其转换为摄氏温度，华氏温度到摄氏温度的转换公式为： C=(F−32)/1.8 


"""
将华氏温度转换为摄氏温度

"""
# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# 说明：上面代码中的input函数用于从键盘接收用户输入，由于输入的都是字符串，
# 如果想处理成浮点小数来做后续的运算，可以用我们上一课讲解的类型转换的方法，用float函数将str类型处理成float类型。

"""
将华氏温度转换为摄氏温度

"""
# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

# 例子2：计算圆的周长和面积
# 要求：输入一个圆的半径（$\small{r}$），计算出它的周长（ 2πr ）和面积（ πr2 ）。

"""
输入半径计算圆的周长和面积

"""
# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * 3.1416 * radius
# area = 3.1416 * radius * radius
# print('周长: %.2f' % perimeter)
# print('面积: %.2f' % area)

"""
输入半径计算圆的周长和面积

"""
# import math

# radius = float(input('请输入圆的半径: '))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius ** 2
# print(f'周长: {perimeter:.2f}')
# print(f'面积: {area:.2f}')

"""
输入半径计算圆的周长和面积

"""
# import math

# radius = float(input('请输入圆的半径: '))  # 输入: 5.5
# perimeter = 2 * math.pi * radius
# area = math.pi * radius ** 2
# print(f'{perimeter = :.2f}')  # 输出：perimeter = 34.56
# print(f'{area = :.2f}')       # 输出：area = 95.03

"""
输入年份，闰年输出True，平年输出False

"""
# year = int(input('请输入年份: '))
# is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# print(f'{is_leap = }')

"""
BMI计算器
"""

# height = float(input('身高(cm): '))
# weight = float(input('体重(kg): '))
# bmi = weight / (height / 100) ** 2
# print(f'{bmi = :.1f}')
# if 18.5 <= bmi < 24:
#     print('好身材！')
# elif bmi < 18.5:
#     print('偏瘦！')
# elif bmi >= 24:
#     print('太重了')
    
#     height = float(input('身高(cm): '))
# weight = float(input('体重(kg): '))
# bmi = weight / (height / 100) ** 2
# print(f'{bmi = :.1f}')
# if 18.5 <= bmi < 24:
#     print('好身材！')
# else:
#     print('身材不在正常范围内哦')
    
# status_code = int(input('响应状态码: '))
# if status_code == 400:
#         description = 'Bad Request'
# elif status_code == 401:
#         description = 'Unauthorized'
# elif status_code == 403:
#         description = 'Forbidden'
# elif status_code == 404:
#         description = 'Not Found'
# elif status_code == 405:
#         description = 'Method Not Allowed'
# elif status_code == 418:
#         description = 'I am a teapot'
# elif status_code == 429:
#         description = 'Too many requests'
# else:
#         description = 'Unknown status Code'
# print('状态码描述:', description)

#下面是使用match-case语法实现的代码，虽然作用完全相同，但是代码显得更加简单优雅。

# status_code = int(input('响应状态码: '))
# match status_code:
#     case 400: description = 'Bad Request'
#     case 401: description = 'Unauthorized'
#     case 403: description = 'Forbidden'
#     case 404: description = 'Not Found'
#     case 405: description = 'Method Not Allowed'
#     case 418: description = 'I am a teapot'
#     case 429: description = 'Too many requests'
#     case _: description = 'Unknown Status Code'
# print('状态码描述:', description)

#当然，match-case语法还有很多高级玩法，其中有一个合并模式可以先教给大家。例如，我们要将响应状态码401、403和404归入一个分支，400和405归入到一个分支，其他保持不变，代码还可以这么写。

# status_code = int(input('响应状态码: '))
# match status_code:
#     case 400 | 405: description = 'Invalid Request'
#     case 401 | 403 | 404: description = 'Not Allowed'
#     case 418: description = 'I am a teapot'
#     case 429: description = 'Too many requests'
#     case _: description = 'Unknown Status Code'
# print('状态码描述:', description)

#分支结构的应用

"""
分段函数求值
# """

# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print(f'{y = }')

# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# else:
#     if x >= -1:
#         y = x - 5
#     else:
#         y = 5 * x + 2
# print(f'{y = }')
## “扁平化”的代码更好，是因为代码嵌套的层次如果很多，会严重的影响代码的可读性

"""
百分制成绩转换为等级制成绩
"""

# score = float(input('请输入成绩'))
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'E'
# print(f'{grade = }')

"""
计算三角形的周长和面积

"""

# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a + b > c and a + c > b and b + c > a:
#     perimeter = a + b + c
#     print(f'周长: {perimeter}')
#     s = perimeter / 2
#     area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     print(f'面积：{area}')
# else:
#     print('不能构成三角形')