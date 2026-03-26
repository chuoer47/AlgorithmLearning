"""
https://www.acwing.com/problem/content/description/169/
"""

import sys

sys.setrecursionlimit(100000)

length = 0  # 木棒设置长度
use = []  # 是否使用过木棒
res = []  # 存储结果
sum_length = 0  # 切断木棒总长度


def dfs(now, s, start):
    """
    :param now: 在拼第几个木棒
    :param s: 当前木棒长度
    :param start: 下标
    :return: 可以完成TRUE，反之FALSE
    """
    global length
    global use
    global sum_length
    if now * length == sum_length:  # 完成拼接
        return True
    if s == length:  # 完成拼接一个木棒的任务，开启下一个
        return dfs(now + 1, 0, 0)
    i = start
    while i < n:
        if use[i]:
            i += 1
            continue
        if lst[i] + s <= length:  # 可以拼接
            use[i] = 1
            if dfs(now, s + lst[i], i + 1):  # 递归查找
                return True
            use[i] = 0
            # 找不到，下面进行剪枝
            if s == 0 or s + lst[i] == length:
                return False
            # 把所有一样的过滤掉
            j = i
            while j < n and lst[j] == lst[i]:
                j += 1
            i = j - 1
        i += 1
    return False


def solve():
    global use
    global length
    global sum_length
    use = [0] * (n + 10)  # 标记是否使用木棒的数组
    sum_length = sum(lst)
    length = max(min(lst), 1)
    while True:
        if sum_length % length == 0 and dfs(0, 0, 0):  # 找到最小的木棒长度
            break
        length += 1
    res.append(length)


while True:
    n = int(input())
    if n == 0:
        break
    lst = list(map(int, input().split(" ")))  # 录入木棒长度
    lst.sort(reverse=True)  # 从大到小排序
    solve()  # 解决单个问题
# 输出结果
for i in range(len(res)):
    print(res[i])
