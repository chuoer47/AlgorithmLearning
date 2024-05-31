"""
https://www.acwing.com/problem/content/1267/
"""


def lowbit(x):
    return x & -x


def add(pivot, x, tr, n):
    while pivot <= n:
        tr[pivot] += x
        pivot += lowbit(pivot)


def getsum(pivot, tr):
    ans = 0
    while pivot:
        ans += tr[pivot]
        pivot -= lowbit(pivot)
    return ans


n = int(input())
lst = [list(map(int, input().split(" "))) for _ in range(n)]
N = 32010
tr = [0] * (N + 10)
res = []
ans = [0] * n
for x, y, in lst:
    add(x + 1, 1, tr, N)
    # 算出每一个星星的星级
    res.append(getsum(x + 1, tr) - 1)
# 整理答案
for r in res:
    ans[r] += 1
# 输出答案
for a in ans:
    print(a)
