"""
https://www.acwing.com/problem/content/507/
"""
import sys

sys.setrecursionlimit(10000)
couple = 0
MOD = 99999997


def re_lst(lst: list):
    """
    该方法将传入的数组进行离散化，把lst变成一个只包含0~n-1的新数组
    :param lst:
    :return:
    """
    p = [(i, lst[i]) for i in range(0, len(lst))]
    p.sort(key=lambda x: x[1])
    for i in range(len(p)):
        lst[p[i][0]] = i


def merge_sort(lst, left, right):
    """
    归并排序
    :param lst:
    :return:
    """
    global couple
    mid = (left + right) // 2
    if left == right:
        return
    merge_sort(lst, left, mid)
    merge_sort(lst, mid + 1, right)

    i = left
    j = mid + 1
    k = left
    while i <= mid and j <= right:
        if lst[i] <= lst[j]:
            tem[k] = lst[i]
            k += 1
            i += 1
        else:
            tem[k] = lst[j]
            k += 1
            j += 1
            couple = (couple + mid - i + 1) % MOD
    while i <= mid:
        tem[k] = lst[i]
        k += 1
        i += 1
    while j <= right:
        tem[k] = lst[j]
        k += 1
        j += 1
    for ii in range(left, right + 1):
        lst[ii] = tem[ii]


n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
# 将数组的范围限制在0~n-1
re_lst(first)
re_lst(second)
# 重新编号
dict_first = {v: i for i, v in enumerate(first)}
for i in range(n):
    first[i] = dict_first[first[i]]
    second[i] = dict_first[second[i]]
# 求second的逆序对即可，利用归并排序
tem = [0 for i in range(n)]
merge_sort(second, 0, n - 1)
print(couple)
