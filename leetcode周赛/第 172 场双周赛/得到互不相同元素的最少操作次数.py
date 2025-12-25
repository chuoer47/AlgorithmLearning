class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = nums[::-1]
        vis = set()
        for i, x in enumerate(nums):
            if x not in vis:
                vis.add(x)
            else:
                # 至少要移除 (n - i) 个元素
                return (n - i + 2) // 3
        return 0
