from cmath import inf
from itertools import accumulate
from typing import List


def helper(nums1, nums2):
    # 实现先完成nums1的项目，然后再完成nums2的项目的情况
    ans = inf
    finish = sorted(x + y for x, y in nums1)
    p = 0
    m = len(finish)
    pi = list(accumulate(finish, func=min))
    for start, dur in nums2:
        while p < m and start >= pi[p]:
            p += 1
        if p > 0:
            ans = min(ans, start + dur)
        if p < m:
            ans = min(ans, pi[p] + dur)
    return ans


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int],
                           waterDuration: List[int]) -> int:
        water = sorted(list(zip(landStartTime, landDuration)))
        land = sorted(list(zip(waterStartTime, waterDuration)))
        ans = min(helper(water, land), helper(land, water))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.earliestFinishTime(
        [71, 73], [47, 84], [99, 66, 60, 20, 63, 39, 36, 91, 77, 40], [28, 79, 25, 90, 67, 52, 66, 66, 89, 27]
    ))
