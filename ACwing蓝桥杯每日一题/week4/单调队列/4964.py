"""
https://www.acwing.com/problem/content/4967/
通过COUNT和堆数据结构取最小值最大值，不过时间复杂度还是很高
"""
from heapq import *
from collections import Counter

MOD = 998244353

n, m, a, b = map(int, input().strip().split(" "))
lst = [list(map(int, input().strip().split(" "))) for _ in range(n)]
res = 0
for i in range(0, n - a+1):
    # 初始化
    cnt = Counter()
    max_heaq = []
    min_heaq = []
    for x in range(i, i + a):
        for y in range(0, b):
            v = lst[x][y]
            cnt[v] += 1
            heappush(min_heaq, v)
            heappush(max_heaq, -v)
    res = (res + (-min_heaq[0] * max_heaq[0])) % MOD
    for j in range(0, m - b):
        for x in range(i, i + a):
            v = lst[x][j]
            cnt[v] -= 1
            v = lst[x][j + b]
            cnt[v] += 1
            heappush(min_heaq, v)
            heappush(max_heaq, -v)
        while cnt[min_heaq[0]] == 0:
            heappop(min_heaq)
        while cnt[-max_heaq[0]] == 0:
            heappop(max_heaq)
        res = (res + (-min_heaq[0] * max_heaq[0])) % MOD
print(res)