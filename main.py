# 归并排序
def mergeSort(lst: list, begin: int, end: int):
    if end == begin:  # 只有一个元素
        return
    mid = (begin + end) >> 1
    mergeSort(lst, begin, mid)
    mergeSort(lst, mid + 1, end)
    l, r = begin, mid + 1
    tem = []
    while l <= mid and r <= end:
        if lst[l] >= lst[r]:
            tem.append(lst[r])
            r += 1
        else:
            tem.append(lst[l])
            l += 1
    if l <= mid:
        tem.extend(lst[l:mid + 1])
    if r <= end:
        tem.extend(lst[r:end + 1])
    lst[begin:end + 1] = tem


def reLst(lst: list):
    t = [(i, lst[i]) for i in range(len(lst))]
    t.sort(key=lambda x: x[1])
    for i in range(len(lst)):
        lst[t[i][0]] = i


if __name__ == '__main__':
    lst = [9, 8, 65, 23, 63, 558, 2, 7777]
    print(lst)
    reLst(lst)

    print(lst)
    mergeSort(lst, 0, len(lst) - 1)
    print(lst)
