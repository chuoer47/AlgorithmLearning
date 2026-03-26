from typing import List


class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        # 线性DP或者贪心
        # 先暴力思路来一发
        # dp[i]表示前i个能够形成平衡装运的最大数量
        # 预处理出来，每一个元素前面比他大的下标即可
        st = [0]  # 维护一个单调递减的单调栈即可满足条件
        n = len(weight)
        dp = [0] * (n + 1)
        for i in range(1, n):
            dp[i] = dp[i - 1]
            while st and weight[st[-1]] <= weight[i]:
                st.pop()
            if st:
                dp[i] = max(dp[i], dp[st[-1] - 1] + 1)
            st.append(i)

        return dp[n - 1]
