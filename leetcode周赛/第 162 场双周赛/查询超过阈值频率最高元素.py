from collections import defaultdict
from typing import List
from math import ceil, sqrt


class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(nums), len(queries)
        cnt = defaultdict(int)
        max_cnt = min_val = 0

        def add(x: int) -> None:
            nonlocal max_cnt, min_val
            cnt[x] += 1
            if cnt[x] > max_cnt:
                max_cnt, min_val = cnt[x], x
            elif cnt[x] == max_cnt:
                min_val = min(min_val, x)

        ans = [-1] * m
        qs = []
        block_size = ceil(n / sqrt(m))
        for i, (l, r, threshold) in enumerate(queries):
            r += 1
            if r - l > block_size:
                qs.append((l // block_size, l, r, threshold, i))
                continue
            for x in nums[l:r]:
                add(x)
            if max_cnt >= threshold:
                ans[i] = min_val
            cnt.clear()
            max_cnt = 0

        qs.sort(key=lambda q: (q[0], q[2]))
        for i, (bid, ql, qr, threshold, qidx) in enumerate(qs):
            l0 = (bid + 1) * block_size
            if i == 0 or bid > qs[i - 1][0]:
                r = l0
                cnt.clear()
                max_cnt = 0
            while r < qr:
                add(nums[r])
                r += 1
            tmp_max_cnt, tmp_min_val = max_cnt, min_val
            for x in nums[ql:l0]:
                add(x)
            if max_cnt >= threshold:
                ans[qidx] = min_val
            max_cnt, min_val = tmp_max_cnt, tmp_min_val
            for x in nums[ql:l0]:
                cnt[x] -= 1
        return ans
