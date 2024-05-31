"""
https://www.acwing.com/problem/content/1225/
"""

import math

n = int(input())
lst = list(map(int, input().split(" ")))
lst = list(set(lst))  # 去重
n = len(lst)
if n == 1:
    print("{}/{}".format(1, 1))
    exit()
lst.sort()
q = []  # 比例
for i in range(1, len(lst)):
    q.append((lst[i], lst[i - 1]))
q.sort(key=lambda x: x[0] / x[1])
for i in range(len(q)):
    a, b = q[i]
    while math.gcd(a, b) != 1:
        t = math.gcd(a, b)
        a //= t
        b //= t
    q[i] = (a, b)
print(q)
