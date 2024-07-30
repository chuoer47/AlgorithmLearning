"""
https://loj.ac/p/134
区间加，单点求
"""


def lowbit(x):
    return x & -x


def add(x, y, v, tr, n, m):
    while x <= n:
        yy = y
        while yy <= m:
            tr[x][yy] += v
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


def real_add(a, b, c, d, k, tr, n, m):
    add(c + 1, d + 1, k, tr, n, m)
    add(a, b, k, tr, n, m)
    add(a, d + 1, -k, tr, n, m)
    add(c + 1, b, -k, tr, n, m)


n, m = map(int, input().split(" "))
tr = [[0] * (m + 10) for _ in range(n + 10)]
while True:
    op = list(map(int, input().split(" ")))
    t, e = op[0], op[1:]
    if t == 1:
        a, b, c, d, k = e
        real_add(a, b, c, d, k, tr, n, m)
    else:
        x, y = e
        print(getSum(x, y, tr))
