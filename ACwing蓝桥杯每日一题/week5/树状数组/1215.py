"""
https://www.acwing.com/problem/content/1217/
使用树状数组解决该问题
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
    for p, i in enumerate(lst):
        add(i, 1, tr, n)
        num[i] += getSum(n,tr) - getSum(i, tr) # 关键步骤
    return


def getReversePairs(lst: list):
    n = len(lst)
    tr = [0] * (n + 10)
    for i in range(n - 1, -1, -1):
        add(lst[i], 1, tr, n)
        num[lst[i]] += getSum(lst[i], tr) - 1 # 关键步骤
    return


n = int(input())
lst = list(map(int, input().strip().split(" ")))
re_lst(lst)
num = [0] * (n + 10)  # 记录交换次数的数组
# 计算逆序
getReversePairs(lst)
# 同上
getPairs(lst)
# 计算结果
res = 0
for v in num:
    res += ((1 + v) * v) // 2
print(res)
