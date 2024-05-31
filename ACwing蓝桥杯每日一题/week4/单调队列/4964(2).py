"""
https://www.acwing.com/problem/content/4967/
"""

from collections import deque

MOD = 998244353


def SlidingWindow(nums: list, k: int, func) -> list:
    q = deque()  # 存取下标
    res = []
    for i in range(k):
        while q and func(nums[q[-1]], nums[i]):
            q.pop()
        q.append(i)
    res.append(nums[q[0]])
    l, r = 1, k
    while r < len(nums):
        rv = nums[r]
        while q and func(nums[q[-1]], rv):
            q.pop()
        q.append(r)
        while q and not l <= q[0] <= r:
            q.popleft()
        res.append(nums[q[0]])
        l, r = l + 1, r + 1
    return res


# 数据录入
n, m, a, b = map(int, input().strip().split(" "))
lst = [list(map(int, input().strip().split(" "))) for _ in range(n)]
res = 0
min_row = []
max_row = []
min_col = []
max_col = []
# 把每行的列最小值/最大值算出来
for i in range(n):
    max_row.append(SlidingWindow(lst[i], b, lambda x, y: x < y))
    min_row.append(SlidingWindow(lst[i], b, lambda x, y: x > y))
for i in range(len(min_row[0])):
    t = [x[i] for x in min_row]
    min_col.append(SlidingWindow(t, a, lambda x, y: x > y))
    t = [x[i] for x in max_row]
    max_col.append(SlidingWindow(t, a, lambda x, y: x < y))
for i in range(len(min_col)):
    for j in range(len(min_col[0])):
        res = (res + (min_col[i][j] * max_col[i][j]) % MOD) % MOD
print(res)