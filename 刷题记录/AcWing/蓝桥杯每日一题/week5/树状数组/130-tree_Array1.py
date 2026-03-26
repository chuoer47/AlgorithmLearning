"""
https://loj.ac/p/130
单点修改，区间查询
"""


def lowbit(x: int):
    return x & -x


def getsum(x):
    ans = 0
    while x > 0:
        ans += c[x]
        x -= lowbit(x)
    return ans


def add(pivot, v):
    while pivot <= n:
        c[pivot] += v
        pivot += lowbit(pivot)


if __name__ == '__main__':
    n, q = map(int, input().strip().split(" "))
    lst = [-1] + list(map(int, input().strip().split(" ")))  # 方便下标操作
    ops = [(map(int, input().strip().split(" "))) for _ in range(q)]
    c = [0] * (n + 10)  # 建立
    res = []
    # 建树
    for i in range(1, n + 1):
        add(i, lst[i])
    del lst
    for op in ops:
        t, x, y = op
        if t == 1:
            add(x, y)
        else:
            res.append(getsum(y) - getsum(x - 1))
    for i in res:
        print(i)
