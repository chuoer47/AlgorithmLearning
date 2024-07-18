"""
https://www.acwing.com/problem/content/1012/
"""


def LIS(weight: list):
    """最长不上升子序列的长度"""
    n = len(weight)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if weight[j] >= weight[i]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)


def LIS_Max(weight: list):
    n = len(weight)
    stack = [weight[0]]
    for i in range(1, n):
        replace = -1
        minV = 99999
        """找到大于weight[i]的最小的序列值，进行替换"""
        for j, v in enumerate(stack):
            if weight[i] <= v <= minV:
                replace = j
                minV = v
        if replace == -1:
            stack.append(weight[i])
        else:
            stack[replace] = weight[i]
    return len(stack)


def LIS_max2(weight: list):
    n = len(weight)
    stack = [weight[0]]
    for i in range(1, n):
        flag = True
        """找到大于weight[i]的最小的序列值，进行替换"""
        for j, v in enumerate(stack):
            if weight[i] <= v:
                stack[j] = weight[i]
                flag = False
                break
        if flag:
            stack.append(weight[i])
    return len(stack)


weight = list(map(int, input().strip().split(" ")))
print(LIS(weight))
# print(LIS_Max(weight))
print(LIS_max2(weight))