"""
https://www.acwing.com/problem/content/3748/
"""


def check(case):
    """
    用来判断case满不满足h指标的要求，满足返回TRUE,不满足返回FALSE
    :param case:
    :return:
    """
    i, j = 0, 0
    for a in arr:
        if a >= case:
            i += 1
        if a >= case - 1:
            j += 1
    # print(min(left,j-i))
    return i + min(left, j - i) >= case


n, left = map(int, input().split())
arr = list(map(int, input().split()))
l, r = 0, n + 100  # 有可能取到n，所以n+100
while l < r:
    mid = (l + r) // 2
    if check(mid):
        l = mid + 1
    else:
        r = mid
print(l - 1)
# print(check(3))
