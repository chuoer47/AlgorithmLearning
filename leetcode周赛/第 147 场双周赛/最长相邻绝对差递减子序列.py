from itertools import accumulate


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # 确定最大值
        mx = max(nums)
        # 确定dp的维数
        max_d = mx - min(nums)
        n = len(nums)
        # dp数组
        dp = [[0] * (max_d + 2) for _ in range(n)]
        # 后缀数组，减少O(D)复杂度
        suffix = [[0] * (max_d + 2) for _ in range(n)]
        last = [-1] * (mx + 1)
        for i, x in enumerate(nums):
            for j in range(max_d, -1, -1):
                dp[i][j] = 1
                if x - j >= 0 and last[x - j] >= 0:
                    dp[i][j] = max(dp[i][j], suffix[last[x - j]][j] + 1)
                if x + j <= mx and last[x + j] >= 0:
                    dp[i][j] = max(dp[i][j], suffix[last[x + j]][j] + 1)
            # 更新后缀数组
            tmp = list(accumulate(dp[i][::-1], max))[::-1]
            suffix[i] = tmp
            last[x] = i
        return max(map(max, dp))
