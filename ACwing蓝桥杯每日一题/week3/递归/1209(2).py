"""
https://www.acwing.com/problem/content/1211/
使用递归解决
"""
from collections import Counter


# 条件是c * target = a * c + b

def check(a, c):
    """
    判断是否满足条件
    :param a:
    :param c:
    :return:
    """
    b = c * target - a * c
    if a == 0 or b == 0 or c == 0:
        return False
    # 下面判断a,b,c是否恰好都用1~9
    lst = list(str(a)) + list(str(b)) + list(str(c))
    lst = [int(i) for i in lst]
    cnt = Counter(lst)
    if cnt[0] != 0:
        return False
    for i in range(1, 10):
        if cnt[i] != 1:
            return False
    return True


def dfs_c(a, c):
    """
    对指定的a，进行c的递归，结果保存到res
    :param a:
    :param c:
    :return:
    """
    global res
    if check(a, c):
        res += 1
    for i in range(1, 10):
        if not use[i]:
            use[i] = True
            dfs_c(a, c * 10 + i)
            use[i] = False


def dfs_a(n):
    """
    对a进行递归
    :param n:
    :return:
    """
    if n >= target:
        return
    if n != 0:
        dfs_c(n, 0)
    for i in range(1, 10):
        if not use[i]:
            use[i] = True
            dfs_a(n * 10 + i)
            use[i] = False


target = int(input())
res = 0
use = [False for i in range(20)] # 判断是否使用的标识数组
dfs_a(0)
print(res)
