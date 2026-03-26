class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        pi = list(accumulate(nums,initial=0))
        ans = inf
        for length in range(l,r+1):
            for i in range(0,n):
                j = i+length
                if j > n:
                    break
                if pi[j]-pi[i] > 0:
                    ans = min(ans,pi[j]-pi[i])
        return ans if ans != inf else -1