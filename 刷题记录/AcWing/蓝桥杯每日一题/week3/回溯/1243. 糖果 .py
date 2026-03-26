"""
https://www.acwing.com/problem/content/description/1245/
"""
import sys

sys.setrecursionlimit(100000)


def contain(x):
    for i in lst[x]:
        if kind[i] == 0:  # 存在没有的元素
            return True
    return False


def add2kind(x):
    for i in lst[x]:
        kind[i] += 1


def sub2kind(x):
    for i in lst[x]:
        kind[i] -= 1


def hasAll():
    r = 0
    for i in range(1, m + 1):
        if kind[i] != 0:
            r += 1
        else:
            return False
    return r == m


def dfs(start):
    global n_bag
    global bag
    if n_bag >= bag:
        return
    if hasAll():
        bag = min(bag, n_bag)
        return
    for i in range(start, n):
        if contain(i):
            add2kind(i)
            n_bag += 1
            dfs(i+1)
            n_bag -= 1
            sub2kind(i)


def check(x):
    v = set()
    for i in range(x, n):
        v = v.union(lst[i])
    return len(v) == m


n, m, k = map(int, input().split(" "))
lst = [list(map(int, input().split(" "))) for _ in range(n)]
verify = []
# 数据预处理
for i in range(n):
    lst[i] = set(lst[i])
    verify += lst[i]
lst.sort(key=lambda x: len(x), reverse=True)
# print(lst)
# 判断能否品尝所有味道
verify = set(verify)
verify = len(verify) == m
if not verify:
    print(-1)
else:
    bag = m  # 最多为m个
    n_bag = 0
    kind = [0] * (m + 10)
    dfs(0)
    print(bag)
