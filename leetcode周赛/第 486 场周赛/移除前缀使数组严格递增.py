class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        nums = nums[::-1]
        pre = inf
        n = len(nums)
        for i in range(n):
            if pre > nums[i]:
                pre = nums[i]
                continue
            return n - i
        return 0