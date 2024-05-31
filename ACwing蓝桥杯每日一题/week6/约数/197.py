"""
https://www.acwing.com/problem/content/199/
"""

from collections import Counter


def findFactor(n):
    for i in range(2, int(n ** 0.5) + 1, 1):
        if i > n:
            break
        if n % i == 0:
            factor.append(i)
            power.append(0)
            while n % i == 0:
                n = n // i
                power[-1] += 1
    if n != 1:
        factor.append(n)
        power.append(1)


n = int(input())
ct = Counter()
ct[2] += 1
for i in range(3, n + 1):
    factor = []
    power = []
    findFactor(i)
    for j in range(len(factor)):
        ct[factor[j]] += power[j]
for i in ct:
    print("{} {}".format(i, ct[i]))
