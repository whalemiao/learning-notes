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

# # # # # # # 325 # # # # # # #

"""
每隔1秒输出一次“hello, world”，持续1小时
"""

# import time

# for _ in range(3600):
#     print('hello, world')
#     time.sleep(1)

"""
从1到100的整数求和
"""

# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

"""
从1到100的偶数求和
"""

# total = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         total += i
# print(total)

# # or

# total = 0
# for i in range(2, 101, 2):
#     total += i
# print(total)

# # 当然， 更为简单的办法是使用 Python 内置的sum函数求和，这样我们连循环结构都省掉了。

# print(sum(range(2, 101, 2)))

# 用while循环来实现从 1 到 100 的整数求和

# total = 0
# i = 1
# while i <= 100:
#     total += i
#     i += 1
# print(total)

# total = 0
# i = 2
# while i <= 100:
#     total += i
#     i += 2
# print(total)

# total = 0
# i = 2
# while True:
#     total += i
#     i += 2
#     if i > 100:
#         break
# print(total)

# total = 0
# for i in range(1, 101):
#     if i % 2 != 0:
#         continue
#     total += i
# print(total)

"""
打印乘法口诀表
"""

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{i}×{j}={i * j}', end='\t')
#     print()

"""
输入一个大于1的正整数判断它是不是素数
"""

# num = int(input('请输入一个正整数'))
# end = int(num ** 0.5)
# is_prime = True
# for i in range(2, end + 1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     if num <= 1:
#         print(f'{num}不是素数')
#     else:
#         print(f'{num}是素数')
# else:
#     print(f'{num}不是素数')

"""
输入两个正整数求它们的最大公约数
"""

# x = int(input('x = '))
# y = int(input('y = '))
# for i in range(x, 0, -1):
#     if x % i == 0 and y % i == 0:
#         print(f'最大公因数：{i}')
#         break

# 用上面代码的找最大公约数在执行效率是有问题的。假如x的值是999999999998，y的值是999999999999，
# 很显然两个数是互质的，最大公约数为 1。但是我们使用上面的代码，循环会重复999999999998次，这通常是难以接受的

# x = int(input('x = '))
# y = int(input('y = '))
# while y % x != 0:
#     x, y = y % x, x
# print(f'最大公因数：{x}')
"""
猜数字小游戏
"""

# import random

# answer = random.randrange(1, 101)
# counter = 0
# while True:
#     try:
#         num = int(input('请输入1~100的数字：'))
#     except ValueError:
#         print('请输入整数')
#         continue
#     if num > 100 or num < 1:
#         print('你输入了1<或>100的数字，请输入1~100的整数')
#         continue
#     counter += 1
#     if num < answer:
#         print('猜小了')
#     elif num > answer:
#         print('猜大了')
#     else:
#         print('You Win')
#         break
# print(f'你一共猜了{counter}次')

# # 这一版是来自Python-100-Days/blob/master/Day01-20/06.循环结构.md中
# # 例子3：猜数字游戏经过ds和我手动的改版

# text = input('请输入字符')

# letters = 0
# number = 0
# space = 0
# other = 0
# for char in text:
#     if char.isalpha():
#         letters += 1
#     elif char.isdigit():
#         number += 1
#     elif char.isspace():
#         space += 1
#     else:
#         other += 1
# print(f'字母:{letters}')
# print(f'数字:{number}')
# print(f'空格:{space}')
# print(f'其他:{other}')

"""
找出所有水仙花数
"""

# for num in range(100, 1000):                       # 遍历所有三位数：100 到 999（range 不包含 1000)
#     low = num % 10                                 # num % 10 取个位数
#     mid = num // 10 % 10                           # 先 // 10 去掉个位，再 % 10 取十位数
#     high = num // 100                              # num // 100 取百位数。
#     if num == low ** 3 + mid ** 3 + high ** 3:     # 判断：个位³ + 十位³ + 百位³ 是否等于原数
#         print(num)                                 # 相等就打印
        
"""
正整数的反转
"""
# num = int(input('num = '))                          # 读取用户输入，转成整数
# reversed_num = 0                                    # 用来存放反转后的结果，初始为 0
# while num > 0:                                      # 只要 num 还有数字没处理完，就继续循环
#     reversed_num = reversed_num * 10 + num % 10     # num % 10：取出 num 的最后一位。
#     reversed_num * 10                               # num % 10：取出 num 的最后一位。reversed_num * 10：把已有的结果整体左移一位（末尾腾出空位）。再加上刚取出的最后一位，就把它拼到了结果的末尾。
#     num //= 10                                      # num // 10 去掉最后一位，准备处理下一位。
# print(reversed_num)                                 # 输出反转后的数。

"""
《百钱百鸡》问题
"""

# for x in range(0, 21):
#     for y in range(0, 34):
#         z = 100 - x - y 
#         if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
#             print(f'公鸡：{x}只， 母鸡：{y}只， 小鸡：{z}只')

# items1 = [35, 12, 99, 68, 55, 35, 87]
# items2 = ['Python', 'Java', 'Go', 'Kotlin']
# items3 = [100, 12.3, 'Python', True]
# print(items1)  # [35, 12, 99, 68, 55, 35, 87]
# print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
# print(items3)  # [100, 12.3, 'Python', True]

# items4 = list(range(1, 10))
# items5 = list('hello')
# print(items4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(items5)  # ['h', 'e', 'l', 'l', 'o']

# items5 = [35, 12, 99, 45, 66]
# items6 = [45, 58, 29]
# items7 = ['Python', 'Java', 'JavaScript']
# print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
# print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
# items5 += items6
# print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]
# print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]
# print(items7 * 2)  # ['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']
# print(29 in items6)  # True
# print(99 in items6)  # False
# print('C++' not in items7)     # True
# print('Python' not in items7)  # False

# items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
# print(items8[0])   # apple
# print(items8[2])   # pitaya
# print(items8[4])   # watermelon
# items8[2] = 'durian'
# print(items8)      # ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
# print(items8[-5])  # 'apple'
# print(items8[-4])  # 'waxberry'
# print(items8[-1])  # watermelon
# items8[-4] = 'strawberry'
# print(items8)      # ['apple', 'strawberry', 'durian', 'peach', 'watermelon']
# print(items8[1:3:1])     # ['strawberry', 'durian']
# print(items8[0:3:1])     # ['apple', 'strawberry', 'durian']
# print(items8[0:5:2])     # ['apple', 'durian', 'watermelon']
# print(items8[-4:-2:1])   # ['strawberry', 'durian']
# print(items8[-2:-6:-1])  # ['peach', 'durian', 'strawberry', 'apple']
# print(items8[1:3])     # ['strawberry', 'durian']
# print(items8[:3:1])    # ['apple', 'strawberry', 'durian']
# print(items8[::2])     # ['apple', 'durian', 'watermelon']
# print(items8[-4:-2])   # ['strawberry', 'durian']
# print(items8[-2::-1])  # ['peach', 'durian', 'strawberry', 'apple
# items8[1:3] = ['x', 'o']
# print(items8)  # ['apple', 'x', 'o', 'peach', 'watermelon']

# nums1 = [1, 2, 3, 4]
# nums2 = list(range(1, 5))
# nums3 = [3, 2, 1]
# print(nums1 == nums2)  # True
# print(nums1 != nums2)  # False
# print(nums1 <= nums3)  # True
# print(nums2 >= nums3)  # False

# languages = ['Python', 'Java', 'C++', 'Kotlin']
# for index in range(len(languages)):
#     print(languages[index])
# # or
# languages = ['Python', 'Java', 'C++', 'Kotlin']
# for language in languages:
#     print(language)

"""
将一颗色子掷6000次，统计每种点数出现的次数
"""
# import random

# counters = [0] * 6
# # 模拟掷色子记录每种点数出现的次数
# for _ in range(6000):
#     face = random.randrange(1, 7)
#     counters[face - 1] += 1
# # 输出每种点数出现的次数
# for face in range(1, 7):
#     print(f'{face}点出现了{counters[face - 1]}次')

# languages = ['Python', 'Java', 'C++']
# languages.append('JavaScript')
# print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']
# languages.insert(1, 'SQL')
# print(languages)  # ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
# languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
# if 'Java' in languages:
#     languages.remove('Java')
# if 'Swift' in languages:
#     languages.remove('Swift')
# print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
# languages.pop()
# temp = languages.pop(1)
# print(temp)       # SQL
# languages.append(temp)
# print(languages)  # ['Python', C++', 'SQL']
# languages.clear()
# print(languages)  # []

# items = ['Python', 'Java', 'C++']
# del items[1]
# print(items)  # ['Python', 'C++']

# items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
# print(items.index('Python'))     # 0
# # 从索引位置1开始查找'Python'
# print(items.index('Python', 1))  # 5
# print(items.count('Python'))     # 2
# print(items.count('Kotlin'))     # 1
# print(items.count('Swfit'))      # 0
# # 从索引位置3开始查找'Java'
# print(items.index('Java', 3))    # ValueError: 'Java' is not in list

# items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
# items.sort()
# print(items)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
# items.reverse()
# print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']

# 场景一：创建一个取值范围在1到99且能被3或者5整除的数字构成的列表。
# items = []
# for i in range(1, 100):
#     if i % 3 == 0 or i % 5 == 0:
#         items.append(i)
# print(items)

# items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
# print(items)

# 场景二：有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方

# nums1 = [35, 12, 97, 64, 55]
# nums2 = []
# for num in nums1:
#     nums2.append(num ** 2)
# print(nums2)

# nums1 = [35, 12, 97, 64, 55]
# nums2 = [num ** 2 for num in nums1]
# print(nums2)

# 场景三： 有一个整数列表nums1，创建一个新的列表nums2，将nums1中大于50的元素放到nums2中。

# nums1 = [35, 12, 97, 64, 55]
# nums2 = []
# for num in nums1:
#     if num > 50:
#         nums2.append(num)
# print(nums2)

# nums1 = [35, 12, 97, 64, 55]
# nums2 = [num for num in nums1 if num > 50]
# print(nums2)

# 嵌套列表,例如：我们想保存5个学生3门课程的成绩，可以用如下所示的列表。

# scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
# print(scores[0])
# print(scores[0][1])

# 如果想通过键盘输入的方式来录入5个学生3门课程的成绩并保存在列表中，可以使用如下所示的代码。

# scores = []
# for _ in range(5):
#     temp = []
#     for _ in range(3):
#         score = int(input('请输入: '))
#         temp.append(score)
#     scores.append(temp)
# print(scores)

# import random

# scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
# print(scores)                 # 产生随机数的方式来生成5个学生3门课程的成绩并保存在列表中

"""
双色球随机选号程序
"""
# import random

# red_balls = list(range(1, 34))
# selected_balls = []
# # 添加6个红色球到选中列表
# for _ in range(6):
#     # 生成随机整数代表选中的红色球的索引位置
#     index = random.randrange(len(red_balls))
#     # 将选中的球从红色球列表中移除并添加到选中列表
#     selected_balls.append(red_balls.pop(index))
# # 对选中的红色球排序
# selected_balls.sort()
# # 输出选中的红色球
# for ball in selected_balls:
#     print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# # 随机选择1个蓝色球
# blue_ball = random.randrange(1, 17)
# # 输出选中的蓝色球
# print(f'\033[034m{blue_ball:0>2d}\033[0m', end=' ')

# 我们还可以利用random模块提供的sample和choice函数来简化上面的代码，前者可以实现无放回随机抽样，后者可以实现随机抽取一个元素，修改后的代码如下所示。

"""
双色球随机选号程序
"""
# import random

# red_balls = [i for i in range(1, 34)]
# blue_balls = [i for i in range(1, 17)]
# # 从红色球列表中随机抽出6个红色球（无放回抽样）
# selected_balls = random.sample(red_balls, 6)
# # 对选中的红色球排序
# selected_balls.sort()
# # 输出选中的红色球
# for ball in selected_balls:
#     print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# # 从蓝色球列表中随机抽出1个蓝色球
# blue_ball = random.choice(blue_balls)
# # 输出选中的蓝色球
# print(f'\033[034m{blue_ball:0>2d}\033[0m')

"""
双色球随机选号程序
"""
# import random

# n = int(input('生成几注号码: '))
# red_balls = [i for i in range(1, 34)]
# blue_balls = [i for i in range(1, 17)]
# for _ in range(n):
#     # 从红色球列表中随机抽出6个红色球（无放回抽样）
#     selected_balls = random.sample(red_balls, 6)
#     # 对选中的红色球排序
#     selected_balls.sort()
#     # 输出选中的红色球
#     for ball in selected_balls:
#         print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
#     # 从蓝色球列表中随机抽出1个蓝色球
#     blue_ball = random.choice(blue_balls)
#     # 输出选中的蓝色球
#     print(f'\033[034m{blue_ball:0>2d}\033[0m')

"""
双色球随机选号程序,没有rich,无法运行
"""
# import random

# from rich.console import Console
# from rich.table import Table

# # 创建控制台
# console = Console()

# n = int(input('生成几注号码: '))
# red_balls = [i for i in range(1, 34)]
# blue_balls = [i for i in range(1, 17)]

# # 创建表格并添加表头
# table = Table(show_header=True)
# for col_name in ('序号', '红球', '蓝球'):
#     table.add_column(col_name, justify='center')

# for i in range(n):
#     selected_balls = random.sample(red_balls, 6)
#     selected_balls.sort()
#     blue_ball = random.choice(blue_balls)
#     # 向表格中添加行（序号，红色球，蓝色球）
#     table.add_row(
#         str(i + 1),
#         f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
#         f'[blue]{blue_ball:0>2d}[/blue]'
#     )

# # 通过控制台输出表格
# console.print(table)