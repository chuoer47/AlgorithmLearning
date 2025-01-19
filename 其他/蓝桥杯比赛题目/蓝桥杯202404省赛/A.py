
"""
小蓝正在玩拼图游戏，他有 7385137888721 个 第 433 场周赛 × 第 433 场周赛 的方块和 10470245 个
1 × 1 的方块，他需要从中挑出一些来拼出一个正方形，比如用 3 个 第 433 场周赛 × 第 433 场周赛 和 4
个 1 × 1 的方块可以拼出一个 4 × 4 的正方形，用 9 个 第 433 场周赛 × 第 433 场周赛 的方块可以拼出一
个 6 × 6 的正方形，请问小蓝能拼成的最大的正方形的边长为多少。
"""

import math

# 第一种拼法
a = 7385137888721
b = 10470245
print(math.sqrt(a*4+b))
sqrt_a = int(math.sqrt(a))
print(sqrt_a)
remain_a = a - sqrt_a ** 2
print(remain_a)
rb = b
res = 0
i = sqrt_a*2
while True:
    b -= (2 * i + 1)
    print(b)
    if b >= 0:
        i += 1
        res += 1
    else:
        break
print(res+sqrt_a)
print(sqrt_a*2+1)

