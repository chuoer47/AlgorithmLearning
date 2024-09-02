from heapq import *
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in nums1:
            for j in nums2:
                if len(heap) < k:
                    heappush(heap, [-(i + j), i, j])
                elif len(heap) == k:
                    v, ii, jj = heappop(heap)
                    v = -v
                    if i + j < v:
                        heappush(heap, [-(i + j), i, j])
                    else:
                        heappush(heap, [-v, ii, jj])
                        break
        ans = [[i, j] for v, i, j in heap]
        return ans
