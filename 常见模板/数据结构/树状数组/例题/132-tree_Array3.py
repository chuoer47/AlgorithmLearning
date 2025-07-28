"""
https://loj.ac/p/132
区间加区间和
"""


def lowbit(x):
    return x & -x


def add(pivot, x, tr, n):
    while pivot <= n:
        tr[pivot] += x
        pivot += lowbit(pivot)


def getsum(pivot, tr):
    ans = 0
    while pivot > 0:
        ans += tr[pivot]
        pivot -= lowbit(pivot)
    return ans


def getAllSum(x, tr_d, tr_di):
    return getsum(x, tr_d) * (x + 1) - getsum(x, tr_di)


n, q = map(int, input().strip().split(" "))
lst = [0] + list(map(int, input().strip().split(" ")))
ops = [list(map(int, input().strip().split(" "))) for _ in range(q)]
tr_d = [0] * (n + 10)
tr_di = [0] * (n + 10)
# 构造差分数组
for i in range(n, 0, -1):
    lst[i] = lst[i] - lst[i - 1]
# 初始化tr_d & tr_di 时间复杂度O(nlogn)
for i in range(1, n + 1):
    add(i, lst[i], tr_d, n)
    add(i, lst[i] * i, tr_di, n)
# 开始操作
for op in ops:
    op_type, t = op[0], op[1:],
    if op_type == 1:
        l, r, x = t
        add(l, x, tr_d, n)
        add(r + 1, -x, tr_d, n)
        add(l, x * l, tr_di, n)
        add(r + 1, -x * (r + 1), tr_di, n)
    else:
        l, r = t
        res = getAllSum(r, tr_d, tr_di) - getAllSum(l - 1, tr_d, tr_di)
        print(res)
