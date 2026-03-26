"""
原题链接：
https://www.acwing.com/problem/content/4659/
该解法使用了堆，优化了一下每次插入堆前的操作，但是还是超时了
"""


def judge(x):
    """
    该函数返回大于等于x的数量s是否大于k
    当s>m,返回False，反之，返回Ture
    :param x:
    :return:
    """
    s = 0
    for i in range(len(arr)):
        a, b = arr[i]
        if a >= x:
            s = s + ((a - x) // b) + 1
    return s <= m


n, m = map(int, input().split(" "))
arr = [list(map(int, input().split(" "))) for i in range(0, n)]
l, r = 0, 10 ** 6
# 找到最小的使judge函数为False的值
while l < r:
    mid = (l + r + 1) // 2
    if judge(mid):
        r = mid - 1
    else:
        l = mid
# print(l, r)
res = 0
case = l
count = 0
# 利用等差数列，计算攻击力
for i in range(len(arr)):
    a, b = arr[i]
    if a >= case:
        dd = (a - case) // b
        count+= dd+1
        res += ((2 * a - b * dd) * (dd + 1)) // 2
print(res-(count-m)*l)
