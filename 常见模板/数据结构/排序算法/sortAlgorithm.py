"""
回顾一下排序算法
写一下选择，归并和快速排序的算法
"""
import numpy as np


def isSorted(lst):
    """判断是否满足排序条件"""
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True


def SelectionSort(lst):
    """选择排序"""
    for i in range(1, len(lst)):
        t = i
        for j in range(i - 1, -1, -1):
            if lst[t] < lst[j]:
                lst[t], lst[j] = lst[j], lst[t]
                t = j
            else:
                break  # 提前结束，减少常数


def mergeSort(lst, left, right):
    """归并排序"""
    if right - left <= 0:
        return
    mid = (left + right) >> 1
    mergeSort(lst, left, mid)
    mergeSort(lst, mid + 1, right)
    i, j = left, mid + 1
    tem = []
    while i <= mid and j <= right:
        if lst[i] < lst[j]:
            tem.append(lst[i])
            i += 1
        else:
            tem.append(lst[j])
            j += 1
    if i <= mid:
        tem.extend(lst[i:mid + 1])
    if j <= right:
        tem.extend(lst[j:right + 1])
    lst[left:right + 1] = tem


def quickSort(lst, left, right):
    """快速排序"""
    if right - left <= 0:
        return
    partition = (left + right) >> 1
    lst[right], lst[partition] = lst[partition], lst[right]
    i, j = left, right - 1
    while i <= j:
        while lst[i] < lst[right] and i <= right:
            i += 1
        while lst[j] >= lst[right] and j >= 0:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[i], lst[right] = lst[right], lst[i]
    quickSort(lst, left, i)
    quickSort(lst, i + 1, right)


if __name__ == '__main__':
    for i in range(0, 10000):
        lst = list(np.random.randint(1, 10000, size=[200]))
        quickSort(lst, 0, len(lst) - 1)
        if not isSorted(lst):
            print("测试失败")
    print("测试成功")
