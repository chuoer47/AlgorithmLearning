"""
https://www.acwing.com/problem/content/1238/
"""

n = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(0, 3)]
for i in arr:
    i.sort(reverse=True)
a, b, c = arr
count = [0 for _ in range(0, n)]

k = 0
j = 0

# 统计b中元素比c的个数
while not (j == n or k == n):
    if b[j] >= c[k]:
        count[j] = k
        j += 1
    else:
        k += 1
if k == n:
    for ii in range(j, n):
        count[ii] = k

# 前缀和构造
for i in range(1, n):
    count[i] = count[i - 1] + count[i]
count = [0]+count

# 计算a,b关系
i, j = 0, 0
res = 0
while not (i == n or j == n):
    if a[i] >= b[j]:
        res += count[j]
        i += 1
    else:
        j += 1
if j == n:
    t = count[-1]
    res += (n - i) * t

print(res)
