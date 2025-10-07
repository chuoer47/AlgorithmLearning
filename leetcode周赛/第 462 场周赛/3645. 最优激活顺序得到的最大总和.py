from typing import List
from heapq import *


class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        hq = [(j, -i) for i, j in zip(value, limit)]
        used = []
        heapify(hq)
        cnt = ans = 0
        while hq:
            while hq and hq[0][0] <= cnt:
                heappop(hq)
            if hq:
                j, i = heappop(hq)
                heappush(used, j)
                i = -i
                ans += i
                cnt += 1
            while hq and hq[0][0] <= cnt:
                heappop(hq)
            while used and used[0] <= cnt:
                cnt -= 1
                heappop(used)
        return ans
