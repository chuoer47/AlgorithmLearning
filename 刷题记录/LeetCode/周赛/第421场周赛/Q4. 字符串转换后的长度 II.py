from typing import List

import numpy as np

mod = int(1e9 + 7)


def qmi(M, k):
    if k == 1:
        return M
    if k % 2 == 0:
        var = qmi(M, k // 2)
        return (np.dot(var, var)) % mod
    return (np.dot(qmi(M, k - 1), M)) % mod


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:

        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1
        M = np.array([[0]*26 for _ in range(26)])
        for i, num in enumerate(nums):
            for j in range(1, num + 1):
                M[i][(i + j) % 26] = 1
        M = qmi(M, t)
        ans = np.dot(cnt, M)
        return int(sum(ans) % mod)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthAfterTransformations(s="azbk", t=1,
                                       nums=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                                             2]))
