"""
https://www.acwing.com/problem/content/1248/
"""

import math

n = int(input())
lst = list(map(int, input().split(" ")))
if n == 1:
    print(1)
    exit()
lst.sort()
d = 0
for i in range(1, n):
    d = math.gcd(lst[i] - lst[i - 1], d)
if d == 0:
    print(n)
else:
    print((lst[-1] - lst[0]) // d + 1)
