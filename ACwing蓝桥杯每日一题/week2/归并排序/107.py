"""
https://www.acwing.com/problem/content/description/109/
"""


def re_lst(lst: list):
    tem = [(i, lst[i]) for i in range(len(lst))]
    tem.sort(key=lambda x: x[1])
    for i in range(n):
        lst[tem[i][0]] = i


def merge_sort(lst, left, right):
    global couple
    if left == right:
        return
    mid = (left + right) // 2
    merge_sort(lst,left,mid)
    merge_sort(lst,mid+1,right)
    i, j = left, mid + 1
    tem = []
    while i <= mid and j <= right:
        if lst[i] <= lst[j]:
            tem.append(lst[i])
            i += 1
        else:
            tem.append(lst[j])
            couple += mid - i + 1
            j += 1
    while i <= mid:
        tem.append(lst[i])
        i += 1
    while j <= right:
        tem.append(lst[j])
        j += 1
    lst[left:right+1] = tem


while True:
    n = int(input())
    if n == 0:
        break
    lst = [int(input()) for i in range(0, n)]
    re_lst(lst)
    couple = 0
    merge_sort(lst, 0, n - 1)
    print(couple)
