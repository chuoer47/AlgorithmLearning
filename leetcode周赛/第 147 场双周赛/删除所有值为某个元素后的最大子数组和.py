from collections import defaultdict
from itertools import accumulate
from typing import List


def maxSubArray(nums: List[int]):
    n = len(nums)
    dp = nums.copy()
    for i in range(1, n):
        dp[i] = max(dp[i], dp[i - 1] + dp[i])
    return dp


class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        nums_set = list(set(nums))
        nums_set.sort()
        # 先特判
        if len(nums_set) == 1 or nums_set[0] >= 0:
            return max(maxSubArray(nums))
        # 前、后缀分解？
        pre = maxSubArray(nums)
        rpre = maxSubArray(nums[::-1])[::-1]
        # 前缀和
        pi = list(accumulate(nums))
        idxs = defaultdict(list)
        for i, v in enumerate(nums):
            idxs[v].append(i)
        ans = max(pre)
        for v in nums_set:
            if v >= 0:
                break
            tmp = []

            x0 = idxs[v][0]
            if x0 > 0:
                tmp.append(pre[x0 - 1])

            n = len(idxs[v])
            # 先考虑区间之间的数字
            for i in range(n - 1):
                x1 = idxs[v][i]
                x2 = idxs[v][i + 1]
                if x1 == x2 - 1:
                    continue
                area = pi[x2] - pi[x1] - nums[x2]
                area2 = pre[x2 - 1]
                if tmp:
                    ans = max(ans, sum(tmp) + rpre[x1] - nums[x1])
                if sum(tmp) + area < area2:
                    tmp = [area2]
                else:
                    tmp.append(area)
            xn = idxs[v][-1]
            if xn < len(nums) - 1:
                tmp.append(rpre[xn + 1])

            print(v, tmp)
            ans = max(ans, max(maxSubArray(tmp)))
        return ans


s = Solution()
print(
    s.maxSubarraySum(nums=[-41, -9, -41, -41, -42]))
