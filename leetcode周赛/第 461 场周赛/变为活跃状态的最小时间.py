from typing import List


class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        # 先特殊判断
        n = len(s)
        if k > n * (n + 1) // 2:
            return -1

        def check(mid):
            vis = set(order[:mid + 1])
            # dp[i][j] 表示以i结尾的字符串，j=0表示无“*”，j=1表示有“*”
            dp = [[0] * 2 for _ in range(n)]
            for i in range(n):
                dp[i][0] = dp[i - 1][0] + 1 if i not in vis else 0
                dp[i][1] = dp[i - 1][1] if i not in vis else dp[i - 1][1] + dp[i - 1][0] + 1
            sn = sum(dp[i][1] for i in range(n))

            return sn >= k

        l, r = 0, n - 1
        ans = n - 1
        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans
