from bisect import bisect_right
from collections import defaultdict


class Solution:
    def maxSubstrings(self, word: str) -> int:
        # 线性dp，dp[i]表示word[:i]不相交的子字符串的最大数量
        idx = defaultdict(list)
        for i, x in enumerate(word):
            idx[x].append(i)
        n = len(word)
        dp = [0] * (n + 1)

        for i in range(3, n):
            dp[i] = dp[i - 1]
            now = idx[word[i]]
            pivot = bisect_right(now, i - 3) - 1  # 3 + 1 >= i - now[pivot] + 1
            if 0 <= pivot < n and i - now[pivot] + 1 >= 4:
                dp[i] = max(dp[i], dp[now[pivot] - 1] + 1)
        return dp[n - 1]
