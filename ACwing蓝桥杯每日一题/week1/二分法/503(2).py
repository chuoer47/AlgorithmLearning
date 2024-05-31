def judge(case):
    """
    判断前case个是否满足借教室的条件，满足返回False，不满足Ture
    :param case:
    :return:
    """
    # 初始化差分数组
    for i in range(len(darr)):
        darr[i] = 0
    # 利用差分数组性质
    for i in range(0, case):
        d, s, j = arr[i]
        darr[s] -= d
        darr[j + 1] += d
    # 还原原始数组
    tem = 0
    for i in range(1, n + 1):
        tem += darr[i]
        if classroom[i] + tem < 0:
            return True
    return False


n, m = map(int, input().split())
classroom = [0] + list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(0, m)]
darr = [0 for i in range(0, n + 10)]
# 先提前判断是否满足
if not judge(m):
    print(0)
    exit(0)
# 发现满足不了，二分法找到第一个出现问题的条件
l = 1
r = m
while l < r:
    mid = (l + r) // 2
    if judge(mid):
        r = mid
    else:
        l = mid + 1
print(-1)
print(l)
