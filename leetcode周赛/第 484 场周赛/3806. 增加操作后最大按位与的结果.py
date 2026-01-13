class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        ans = 0
        n = len(nums)
        cost = [0] * n
        for bit in range(32, -1, -1):
            target = ans | (1 << bit)
            for i, v in enumerate(nums):
                # 找到第j为不匹配的bit
                j = (target & ~v).bit_length()
                mask = (1 << j) - 1
                cost[i] = (target & mask) - (v & mask)
            cost.sort()
            if sum(cost[:m]) <= k:
                ans = target
        return ans