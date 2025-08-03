from cmath import inf
from typing import List
from collections import defaultdict
from math import isqrt


class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        q_size = len(queries)
        block_size = isqrt(n) + 1
        # 静态查询，提前预处理
        table_q = [(li, ri, threshold, idx) for idx, (li, ri, threshold) in enumerate(queries)]

        def mo_cmp(query):
            li, ri, _, _ = query
            block = li // block_size
            return block, ri

        table_q.sort(key=mo_cmp)

        ans = [-1] * q_size
        freq = defaultdict(int)
        cnt = defaultdict(int)
        mf = 0
        l, r = 0, -1

        for li, ri, threshold, idx in table_q:
            # 先扩张后收缩防止出现问题
            while r < ri:
                r += 1
                val = nums[r]
                old = freq[val]
                if old > 0:
                    cnt[old] -= 1
                freq[val] += 1
                new = old + 1
                cnt[new] += 1
                if new > mf:
                    mf = new

            while r > ri:
                val = nums[r]
                old = freq[val]
                cnt[old] -= 1
                freq[val] -= 1
                new = old - 1
                if new > 0:
                    cnt[new] += 1
                if old == mf and cnt[old] == 0:
                    mf = max(cnt.keys()) if cnt else 0
                r -= 1

            while l < li:
                val = nums[l]
                old = freq[val]
                cnt[old] -= 1
                freq[val] -= 1
                new = old - 1
                if new > 0:
                    cnt[new] += 1
                if old == mf and cnt[old] == 0:
                    mf = max(cnt.keys()) if cnt else 0
                l += 1

            while l > li:
                l -= 1
                val = nums[l]
                old = freq[val]
                if old > 0:
                    cnt[old] -= 1
                freq[val] += 1
                new = old + 1
                cnt[new] += 1
                if new > mf:
                    mf = new

            best_f = -1
            for f in range(mf, threshold - 1, -1):
                if cnt[f] > 0:
                    best_f = f
                    break

            if best_f == -1:
                ans[idx] = -1
            else:
                min_num = inf
                for val in freq:
                    if freq[val] == best_f and val < min_num:
                        min_num = val
                ans[idx] = min_num

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.subarrayMajority(nums=[3, 2, 3, 2, 3, 2, 3], queries=[[0, 6, 4], [1, 5, 2], [2, 4, 1], [3, 3, 1]]))
