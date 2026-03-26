class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n+1
        l,r = 0,0
        total = 0
        while r<n:
            total+=nums[r]
            while total>=target:
                ans = min(ans,r-l+1)
                total-=nums[l]
                l+=1
            r+=1
        return 0 if ans==n+1 else ans