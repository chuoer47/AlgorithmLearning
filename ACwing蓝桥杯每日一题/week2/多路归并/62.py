"""
https://www.acwing.com/file_system/file/content/whole/index/content/3607/
"""
from math import inf

n = int(input())
num = [2, 3, 5]
pivot = [0] * 3  # 记录三个质因子2,3,5的下标
lst = [1]  # 存储丑数
for i in range(0, n - 1):
    next = inf  # 下一个丑数
    for p in range(0, 3):
        # print(p)
        v = num[p] * lst[pivot[p]]
        if v < next:
            next = min(next, v)
    for p in range(3):
        v = num[p] * lst[pivot[p]]
        if v == next:
            pivot[p] += 1
    lst.append(next)
# print(pivot)
# print(lst)
print(lst[-1])
