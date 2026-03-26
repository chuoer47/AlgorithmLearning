"""
https://www.luogu.com.cn/problem/P3865
"""
from math import log2, ceil

# 数据录入

n, m = map(int, input().strip().split(" "))
a = list(map(int, input().strip().split(" ")))
query = [list(map(int, input().strip().split(" "))) for _ in range(m)]

# 预处理ST表，即f数组
x, y = n, ceil(log2(m + 1))  # 确定数组大小
# x, y = n, 21
f = [[0] * y for _ in range(x)]  # 创建数组
for i in range(n):
    f[i][0] = a[i]

# 预处理log2的表，减少运算
logLst = [0, 0, 1, ]
for i in range(3, n + 10):
    logLst.append(logLst[i >> 1] + 1)

for j in range(1, y):
    for i in range(n):
        if i + (1 << (j - 1)) < n:
            f[i][j] = max(f[i][j - 1], f[i + (1 << (j - 1))][j - 1])

res = []
for l, r in query:
    l, r = l - 1, r - 1
    s = logLst[r - l + 1]
    res.append(max(f[l][s], f[r - (1 << s) + 1][s]))
for i in res:
    print(i)
