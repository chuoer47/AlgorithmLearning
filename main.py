from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        w = [[v, i] for i, v in enumerate(nums)]
        w.sort()
        for pw,ww in enumerate(w[:-1]):
            v,i = ww
            if v == w[pw + 1][0]:
                if abs(i - w[pw + 1][1]) <= k:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))
