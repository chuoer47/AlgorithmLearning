"""
https://www.acwing.com/problem/content/104/
"""


def check(case):
    """
    用来判断在arr中平均值最大能否达到case
    能达到返回TRUE,不嫩返回FALSE
    :param case:
    :return:
    """
    # 构造前缀和数组
    for i in range(1, n + 1):
        d_arr[i] = d_arr[i - 1] + arr[i] - case
    # 双指针检验
    left, right = 0, f
    min_left = d_arr[left]
    while right <= n:
        min_left = min(min_left, d_arr[left])
        if d_arr[right] - min_left >= 0:
            return True
        left += 1
        right += 1
    return False


n, f = map(int, input().split())
arr = [0 for _ in range(0, n + 10)]
for i in range(1, n + 1):
    arr[i] = int(input())
d_arr = [0 for _ in range(0, n + 10)]  # 前缀和数组
#   使用二分法寻找最大值，这个设计很巧妙
l, r = 0, max(arr)
while r - l > 1e-6:
    mid = (r + l) / 2
    if check(mid):
        l = mid
    else:
        r = mid
# print(l, r)

print(int(r * 1000))
