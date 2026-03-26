"""
https://www.acwing.com/problem/content/description/3421/
"""
from math import inf

n = int(input())


def C(a, b):
    """由于b<a//2,保证了递增，因此可以用ans > n"""
    ans = 1
    for i, j in zip(range(a, -1, -1), range(1, b + 1, 1)):
        ans = ans * i // j
        if ans > n:
            return inf
    return ans


def find(k):
    l, r = 0, n
    # 二分找到最小的大于n的值
    while l < r:
        m = (l + r) // 2
        if C(m, k) >= n:
            r = m
        else:
            l = m + 1
    if C(l, k) != n:
        return -1
    return l * (l + 1) // 2 + k + 1


# 二分求解，找最小序号
res = inf
for k in range(16, -1, -1):
    c = find(k)
    if c != -1:
        res = min(res, c)
print(res)
