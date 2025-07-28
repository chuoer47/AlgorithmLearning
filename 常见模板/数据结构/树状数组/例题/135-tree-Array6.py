"""
https://loj.ac/p/135
区间修改，区间求和
"""


def lowbit(x):
    return x & -x


def add(x, y, k, n, m):
    i = x
    while i <= n:
        j = y
        while j <= m:
            tr_d[i][j] += k
            tr_di[i][j] += k * x
            tr_dj[i][j] += k * y
            tr_dij[i][j] += k * x * y
            j += lowbit(j)
        i += lowbit(i)


def addRange(a, b, c, d, k):
    """差分加"""
    add(c + 1, d + 1, k, n, m)
    add(a, b, k, n, m)
    add(c + 1, b, -k, n, m)
    add(a, d + 1, -k, n, m)


def getSum(x, y):
    ans = 0
    i = x
    while i:
        j = y
        while j:
            ans += (x + 1) * (y + 1) * tr_d[i][j] - (y + 1) * tr_di[i][j] - (x + 1) * tr_dj[i][j] + tr_dij[i][j]
            j -= lowbit(j)
        i -= lowbit(i)
    return ans


def getRangeSum(xa, ya, xb, yb):
    return getSum(xb, yb) - getSum(xb, ya - 1) - getSum(xa - 1, yb) + getSum(xa - 1, ya - 1)


n, m = map(int, input().split(" "))
tr_d = [[0] * (m + 10) for _ in range(n + 10)]  # d(i,j)
tr_di = [[0] * (m + 10) for _ in range(n + 10)]  # d(i,j)*i
tr_dj = [[0] * (m + 10) for _ in range(n + 10)]  # d(i,j)*j
tr_dij = [[0] * (m + 10) for _ in range(n + 10)]  # d(i,j)*i*j

while True:
    op = list(map(int, input().split(" ")))
    t, e = op[0], op[1:]
    if t == 1:
        a, b, c, d, x = e
        addRange(a, b, c, d, x)
    else:
        a, b, c, d = e
        print(getRangeSum(a, b, c, d))