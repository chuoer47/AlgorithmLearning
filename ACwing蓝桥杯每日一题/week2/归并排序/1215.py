"""
https://www.acwing.com/problem/content/1217/
"""


def re_lst(lst: list):
    p = [(i, p) for i, p in enumerate(lst)]
    p.sort(key=lambda x: x[1])
    for i in range(len(lst)):
        lst[p[i][0]] = i


def merge_sort(lst, left, right):
    if left == right:
        return
    mid = (left + right) // 2
    merge_sort(lst, left, mid)
    merge_sort(lst, mid + 1, right)
    i, j, k = left, mid + 1, left
    while i <= mid and j <= right:
        if lst[i] <= lst[j]:
            tem[k] = lst[i]
            dict_lst[lst[i]] += j - (mid + 1)
            k += 1
            i += 1
        else:
            tem[k] = lst[j]
            dict_lst[lst[j]] += mid-i+1
            j += 1
            k += 1
    while i <= mid:
        tem[k] = lst[i]
        dict_lst[lst[i]] += j - (mid + 1)
        k += 1
        i += 1
    while j <= right:
        tem[k] = lst[j]
        dict_lst[lst[j]] += mid-i+1
        k += 1
        j += 1
    for ii in range(left, right + 1):
        lst[ii] = tem[ii]


n = int(input())
lst = list(map(int, input().split()))
re_lst(lst)
print(lst)
tem = [0 for i in range(0, n)]
dict_lst = {i: 0 for i in range(0, n)}
merge_sort(lst, 0, n - 1)
res = 0
print(dict_lst)
for v in dict_lst.values():
    res += ((1+v)*v) // 2
print(res)