"""
https://www.acwing.com/problem/content/1211/
暴力解法，看题解的
"""
import itertools


def cal(l, r):
    res = 0
    for i in range(l + 1, r + 1):
        res = sub_lst[i] + res * 10
    return res


n = input()
length = len(n)
target = int(n)
lst = [i for i in range(1, 10)]
arr = itertools.permutations(lst)  # 利用全排序
res = 0
sub_lst = []
for sub_lst in arr:
    for i in range(0, length):
        for j in range(i + 1, 9):
            a = cal(-1, i)
            # 剪枝
            if a >= target:
                break
            b = cal(i, j)
            c = cal(j, 8)
            if target * c == a * c + b:
                res += 1
print(res)
