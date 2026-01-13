class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        # 滑动窗口 + 遍历；O(n^2)的操作
        n = len(nums)
        def helper(start):
            s = set()
            sn = ans = 0
            for i in range(start,n):
                x = nums[i]
                s.add(x)
                sn += x
                if sn in s:
                    ans += 1
            return ans
        return sum(helper(i) for i in range(n))