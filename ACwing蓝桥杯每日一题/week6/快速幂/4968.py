"""
https://www.acwing.com/problem/content/4971/
"""
from math import gcd
from math import sqrt


def solve(x):
    """求解x的质因数分解"""
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            factor.append(i)
            p.append(1)
            x = x // i
            while x % i == 0:
                p[-1] += 1
                x = x // i
    if x != 1:
        factor.append(x)
        p.append(1)


a, b = map(int, input().split(" "))
if a == 1 or b == 0: # 特判
    print(0)
    exit()
MOD = 998244353
factor = []
p = []
solve(a)
# 欧拉函数
a_b1 = pow(a, b-1, MOD)
res = a
for pivot, f in enumerate(factor):
    res = res * ((f - 1) // f)
res = (res * a_b1) % MOD
print(res)
