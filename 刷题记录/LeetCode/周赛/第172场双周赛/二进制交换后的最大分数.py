class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        # 反悔堆？
        n = len(nums)
        nums = nums[::-1]
        s = s[::-1]
        hq = []
        for i,j in zip(nums,s):
            if j == '1':
                heappush(hq,i)
            else:
                if hq and hq[0] < i:
                    heapreplace(hq,i)
        return sum(hq)

