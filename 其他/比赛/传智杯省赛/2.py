from collections import deque


def helper(nums):
    # dp[i][j]表示以第i个为结尾，j表示是否使用消失的字符，属性为满足条件的最大长度
    n = len(nums)
    mx = n + 1
    dp = [[1] * 2 for _ in range(n)]
    ans = 2  # ans最少也得是2
    for i in range(n):
        dp[i][1] = 1 if nums[i] == 1 else 2  # 开头特殊情况
    for i in range(1, n):
        dp[i][0] = max(dp[i][0],
                       dp[i - 1][0] + 1 if nums[i - 1] + 1 == nums[i] else 0)  # 正常情况 +1
        dp[i][1] = max(dp[i][1],
                       dp[i - 1][1] + 1 if nums[i - 1] + 1 == nums[i] else 0,  # 正常情况+1
                       dp[i][0],  # 这个是不是有问题？ 假设 1 2 3 4 1 3
                       dp[i - 1][0] + 2 if nums[i - 1] + 2 == nums[i] else 0)  # 使用 +2
        ans = max(ans,
                  dp[i][0] + (1 if nums[i] < mx else 0),  # 结尾特殊情况
                  dp[i][1])
    return ans


T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    print(helper(nums))
