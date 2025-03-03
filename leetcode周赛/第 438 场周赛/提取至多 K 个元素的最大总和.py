from heapq import heappop, heappush, heapify
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        # 贪心找出所有矩阵
        hq = []
        for i, row in enumerate(grid):
            row.sort(reverse=True)
            hq.append((-row[0], i, 0))
        heapify(hq)
        n, m = len(grid), len(grid[0])
        ans = 0
        for _ in range(k):
            v, i, pivot = heappop(hq)
            ans -= v
            if pivot + 1 < limits[i]:
                heappush(hq, (-grid[i][pivot + 1], i, pivot + 1))
        return ans


s = Solution()
print(s.maxSum(grid=[[1, 2], [3, 4]], limits=[1, 2], k=2))
