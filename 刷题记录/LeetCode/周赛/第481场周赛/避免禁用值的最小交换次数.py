class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        # 1e5的数据范围，应该是贪心 + 线性时间复杂度求解
        # 1.极端情况开始考虑，不管如何交换都没有办法满足条件：
        n = len(nums)
        match = list(i for i,j in zip(nums,forbidden) if i == j)
        if not match:
            return 0
        cnt1 = Counter(nums)
        cnt2 = Counter(forbidden)
        for k,v in cnt2.items():
            if cnt1[k] > n - v:
                return -1
        mx = max(Counter(match).values())
        return max(mx, (len(match) + 1) // 2)