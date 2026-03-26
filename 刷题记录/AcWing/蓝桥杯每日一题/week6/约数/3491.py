"""
https://www.acwing.com/problem/content/3494/
"""


def findFactor(n):
    for i in range(2, int(n ** 0.5) + 1, 1):
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
if n <= 3:  # 特判一下
    print(n)
    exit()
factor = []
power = []
findFactor(n)
res = 1
for i in range(len(factor)):
    if power[i] % 2 == 1:
        res *= factor[i]
print(res)
