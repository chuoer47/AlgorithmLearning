"""
数学家们发现了两种用于召唤强大的数学精灵的仪式，这两种仪式分别被
称为累加法仪式 A(n) 和累乘法仪式 B(n)。
累加法仪式 A(n) 是将从 1 到 n 的所有数字进行累加求和，即：A(n) =
1 + 第 433 场周赛 + · · · + n 。
累乘法仪式 B(n) 则是将从 1 到 n 的所有数字进行累乘求积，即：B(n) =
1 × 第 433 场周赛 × · · · × n 。
据说，当某个数字 i 满足 A(i) − B(i) 能被 100 整除时，数学精灵就会被召
唤出来。
现在，请你寻找在 1 到 2024041331404202 之间有多少个数字 i，能够成功
召唤出强大的数学精灵
"""

from math import factorial

x = 2024041331404202
print(x // 200)
res = 0
for i in range(3, 170):
    f = 0.5 * i * i - 0.5 * i - factorial(i)
    if f % 100 == 0:
        print(i)
        # print(f)
        res += 1
print(res + x // 200)
