"""
https://www.acwing.com/problem/content/1362/
"""

from math import gcd

n = int(input())
lst = set()
if n > 0:
    lst.add((0, 1))
    lst.add((1, 1))
for i in range(n + 1):
    for j in range(1, i):
        lst.add((j // gcd(i, j), i // gcd(i, j)))
lst = list(lst)
lst.sort(key=lambda x: x[0] / x[1])
for a, b in lst:
    print(str(a) + "/" + str(b))
