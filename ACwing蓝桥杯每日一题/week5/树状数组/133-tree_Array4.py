"""
https://loj.ac/p/133
单点修改，区间查询
"""


def lowbit(x):
    return x & -x


def add(x, y, k, tr, n, m):
    """再(x,y)矩阵添加k"""
    while x <= n:
        yy = y
        while yy <= m:
            tr[x][yy] += k
            yy += lowbit(yy)
        x += lowbit(x)


def getSum(x, y, tr):
    ans = 0
    while x:
        yy = y
        while yy:
            ans += tr[x][yy]
            yy -= lowbit(yy)
        x -= lowbit(x)
    return ans


n, m = map(int, input().split(" "))
tr = [[0] * (m + 10) for _ in range(n + 10)]
while True:
    op = list(map(int, input().split(" ")))
    t, e = op[0], op[1:],
    if t == 1:
        x, y, k = e
        add(x, y, k, tr, n, m)
    else:
        a, b, c, d = e
        print(getSum(c, d, tr) - getSum(a - 1, d, tr) - getSum(c, b - 1, tr) + getSum(a - 1, b - 1, tr))
