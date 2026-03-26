from typing import List


class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        mx = (n + 1) * n // 2
        if target > mx or target < -mx:
            return []
        ans = [i for i in range(1, n + 1)][::-1]
        diff = mx - target
        left = 0
        while diff > 0:
            if diff >= 2 * ans[left]:
                ans[left] = -ans[left]
                diff -= 2 * ans[left]
            left -= 1
        return sorted(ans)
