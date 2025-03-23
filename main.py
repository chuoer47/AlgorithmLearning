# coding = gb1231
from typing import List


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        nums = []
        for i in range(0, 32):
            nums.append(1 << i)

        def helper(x):
            m = x.bit_length()
            ans = sum((i + 1) // 2 << (i - 1) for i in range(1, m))
            return ans + (m + 1) // 2 * (x + 1 - (1 << m >> 1))

        ans = sum((helper(r) - helper(l - 1) + 1) // 2 for l, r in queries)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(queries=[[1, 2], [2, 4]]))
