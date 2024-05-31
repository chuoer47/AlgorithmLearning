"""
小蓝在无聊时随机生成了一个长度为 n 的整数数组，数组中的第 i 个数为
ai，他觉得随机生成的数组不太美观，想把它变成回文数组，也是就对于任意
i ∈ [1, n] 满足 ai = an−i+1 。小蓝一次操作可以指定相邻的两个数，将它们一起加
1 或减 1 ；也可以只指定一个数加 1 或减 1 ，请问他最少需要操作多少次能把
这个数组变成回文数组？
"""
from math import inf


def sgn(n, ln):
    if n > 0 and ln > 0:
        return "+"
    elif n < 0 and ln < 0:
        return "-"
    else:
        return "None"


def dfs(pivot):
    if pivot >= len(lst):
        return
    global res, final
    n, ln = lst[pivot], lst[pivot - 1]
    final = min(final, res + sum(map(abs, lst)))
    if sgn(n, ln) == "+":  # 同号
        min_t = min(n, ln)
        lst[pivot] -= min_t
        lst[pivot - 1] -= min_t
        res += min_t
        final = min(final, res + sum(map(abs, lst)))
        dfs(pivot + 1)  # 递归
        # 还原现场
        lst[pivot] += min_t
        lst[pivot - 1] += min_t
        res -= min_t
    elif sgn(n, ln) == "-":
        max_t = max(n, ln)
        lst[pivot] -= max_t
        lst[pivot - 1] -= max_t
        res -= max_t
        final = min(final, res + sum(map(abs, lst)))
        dfs(pivot + 1)  # 递归
        # 还原现场
        lst[pivot] += max_t
        lst[pivot - 1] += max_t
        res += max_t
    # print(lst)
    dfs(pivot + 1)  # 递归


n = int(input())
lst = list(map(int, input().split(" ")))
# 数据预处理
first = []
second = []
if n % 2 == 0:  # 偶数
    first = lst[:n // 2]
    second = lst[n // 2:]
else:
    first = lst[:n // 2]
    second = lst[n // 2 + 1:]
second.reverse()
for i in range(len(first)):
    first[i] = first[i] - second[i]
lst = first
# 下面进行暴搜，差分的方法想不出来，我不确定差分能不能求解
res = 0
final = inf
dfs(0)
print(final)
