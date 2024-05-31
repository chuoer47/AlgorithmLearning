"""
https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
求逆序对
"""


def re_lst(lst):
    """离散化数组"""
    tem = [(pivot, i) for pivot, i in enumerate(lst)]
    tem.sort(key=lambda x: x[1])
    for i in range(len(tem)):
        lst[i] = tem[i][0] + 1  # 从1开始，方便树状数组


def lowbit(x):
    return x & -x


def add(pivot, x, tr, n):
    while pivot <= n:
        tr[pivot] += x
        pivot += lowbit(pivot)


def getSum(pivot, tr):
    ans = 0
    while pivot:
        ans += tr[pivot]
        pivot -= lowbit(pivot)
    return ans


def getPairs(lst):
    """顺序对"""
    n = len(lst)
    tr = [0] * (n + 10)
    ans = 0
    for p, i in enumerate(lst):
        add(i, 1, tr, n)
        ans += getSum(i, tr) - 1
    return ans


def getReversePairs(lst: list):
    n = len(lst)
    tr = [0] * (n + 10)
    ans = 0
    for i in range(n - 1, -1, -1):
        add(lst[i], 1, tr, n)
        ans += getSum(lst[i], tr) - 1
    return ans


lst = [4, 3, 2, 1]
re_lst(lst)
print(lst)
# 先求顺序对
t = getPairs(lst)
print(t)
# 求逆序对
print(getReversePairs(lst))
