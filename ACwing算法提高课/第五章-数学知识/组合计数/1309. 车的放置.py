"""
https://www.acwing.com/problem/content/1311/
"""

import math

mod = 100003


def C(m, n):
    return (math.factorial(n) // (math.factorial(m) * math.factorial(n - m))) % mod


def A(m, n):
    return (math.factorial(n) // math.factorial(n - m)) % mod


a, b, c, d, k = map(int, input().strip().split(" "))

ans = 0
for i in range(0, min(k, b, a) + 1):
    if k - i <= min(a + c - i, d):
        ans = (ans + C(i, b) * A(i, a) * C(k - i, d) * A(k - i, a + c - i)) % mod

print(ans)
