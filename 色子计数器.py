# # 单色子
# import random

# times = [0] * 6
# counters = random.randrange(1000, 10000)
# for _ in range(counters):
#     y = random.randrange(1, 7)
#     times[y - 1] += 1
# print(f'次数：{counters}')
# for y in range(1, 7):
#     print(f'{y}点出现了{times[y - 1]}次，占{times[y - 1] / counters * 100:.2f}%')


# # 双色子
# import random

# times = [0] * 11
# counters = random.randrange(10000, 10000)
# for _ in range(counters):
#     y = random.randrange(2, 13)
#     times[y - 2] += 1
# print(f'次数：{counters}')
# for y in range(2, 13):
#     print(f'{y}点出现了{times[y - 2]}次，占{times[y - 2] / counters * 100:.2f}%')
    
# 六个色子，正态分布，更加接近真实色子

import random

times = [0] * 31
counters = random.randrange(10000, 100000)
for _ in range(counters):
    y = sum(random.randrange(1, 7) for _ in range(6))
    times[y - 6] += 1
print(f'次数：{counters}')
for y in range(6, 37):
    print(f'{y}点出现了{times[y - 6]}次，占{times[y - 6] / counters * 100:.2f}%')

