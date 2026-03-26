"""
https://www.acwing.com/problem/content/5410/
"""
import bisect


def sgn(x):
    """
    进行边界条件判断的函数
    :param x:
    :return:
    """
    if x <= 0:
        return 1
    elif x >= length:
        return length
    else:
        return x


def judge(case):
    """
    判断case时刻是否都有水流，有返回TRUE,无返回FALSE
    :param case:
    :return:
    """
    # 初始化状态数组
    state = []
    # 确定水流
    for i in range(0, n):
        if case < S[i]:  # 还没有开闸
            continue
        l, r = sgn(L[i] - (case - S[i])), sgn(L[i] + (case - S[i]))
        state.append((l, r))
    state.sort()
    # print(case,state)
    # 下面的代码用来判断是否所有段存在水流，时间复杂度O(n)
    l, r = state[0][0], state[0][1]
    if l != 1:
        return False
    for i in range(1, len(state)):
        ll, rr = state[i]
        if ll > r+1:
            return False
        else:
            r = max(rr, r)
    return (l == 1) and (r == length)


n, length = map(int, input().split(" "))
arr = [list(map(int, input().split(" "))) for i in range(0, n)]
# darr = [0 for _ in range(0, length + 10)]  # 构造差分数组
L = [arr[i][0] for i in range(0, n)]
S = [arr[i][1] for i in range(0, n)]
# print(arr,L,S)
# 利用二分法找到最早有水流的时间
l, r = 1, min(S) + length
while l < r:
    mid = (l + r) // 2
    if judge(mid):  # 有水流
        r = mid
    else:  # 无水流
        l = mid + 1
print(l)