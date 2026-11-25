import random

times = [0] * 6
counters = random.randrange(1000, 10000)
for _ in range(counters):
    y = random.randrange(1, 7)
    times[y - 1] += 1
print(f'次数：{counters}')
for y in range(1, 7):
    print(f'{y}点出现了{times[y - 1]}次，占{times[y - 1] / counters *100:.2f}%')
    
    