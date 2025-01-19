from cmath import inf
from typing import List


class Solution:
    def minCost(
            self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int
    ) -> int:
        dp = [[[inf] * (target + 1) for _ in range(n)] for _ in range(m)]
        # 初始化
        if houses[0] == 0:
            for i in range(n):
                dp[0][i][1] = cost[0][i]
        else:
            dp[0][houses[0] - 1][1] = 0

        for i in range(1, m):
            choose = [houses[i] - 1] if houses[i] != 0 else range(0, n)
            _nc = [0] if houses[i] != 0 else cost[i]
            for color1, nc in zip(choose, _nc):
                for color2 in range(0, n):
                    for j in range(1, target + 1):
                        if dp[i - 1][color2][j] == inf:
                            continue
                        if color1 == color2:
                            dp[i][color1][j] = min(dp[i][color1][j], dp[i - 1][color2][j] + nc)
                        else:
                            dp[i][color1][j] = min(dp[i][color1][j], dp[i - 1][color2][j - 1] + nc)

        ans = min(dp[m - 1][color][target] for color in range(0, n))
        return ans if ans != inf else -1
