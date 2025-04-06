from cmath import inf
from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def check(nums):
            n = len(nums)
            return all(nums[i] <= nums[i + 1] for i in range(n - 1))

        ans = 0
        while not check(nums):
            ans += 1
            n = len(nums)
            nxt = []
            mn = inf
            idx = -1
            for i in range(n - 1):
                if nums[i] + nums[i + 1] < mn:
                    mn = nums[i] + nums[i + 1]
                    idx = i
            i = 0
            while i < n:
                if i != idx:
                    nxt.append(nums[i])
                    i += 1
                else:
                    nxt.append(nums[i] + nums[i + 1])
                    i += 2
            nums = nxt
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minimumPairRemoval([5, 2, 3, 1]))
