# 做法如下：
# 1.对于每一个位置i，求出恰好有k个元素的对应下标j(j<=i)
# len(set(nums[j:i + 1])) == k
# 假设最左边的为 left_j,最右边的为 right_j
# 可以使用至多型滑动窗口(k/k-1)求取下标
# 2.对于每一个位置i，确定了k个元素，对于这k个元素，去找满足至少出现m次的idx_i(i=1,2,....k)
# 最左边的idx_i记为idx_l,最右边的idx_i记为idx_r
# ans += max(0,min(idx_l,right_j) - left_j + 1)
# ======================
# 估算时间复杂度
# 步骤1时间复杂度为O(n)
# 步骤2的难点在于与 k 个元素强相关的话，会导致时间复杂度为O(n*k),甚至更加糟糕的复杂度
# 步骤2的idx可以预处理 + 二分查找找出来，logn的时间复杂度
# 需要维护一个特殊的数据结构，在步骤2进行o(n)遍历的时候，只维护最新的k个整数的idx,可以在较快的时间内查询出来这k个idx的最大值和最小值
# 最大值/最小值的查询可以使用懒删除堆维护，时间复杂度logk；维护最新的k个整数可以使用双指针


from collections import defaultdict, deque
import heapq
from typing import Optional


class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        if k <= 0 or m <= 0:
            return 0

        # occ[x] stores all occurrence indices of value x (in increasing order).
        occ: dict[int, deque[int]] = defaultdict(deque)
        # pos_m[x] is the index of the m-th latest occurrence of x seen so far.
        pos_m: dict[int, int] = {}
        # Min-heap of (pos_m[x], x) for fast global minimum; lazy deletion on stale entries.
        heap: list[tuple[int, int]] = []

        # counts_k is the frequency table for the "at most k distinct" window [left_k, r].
        counts_k: dict[int, int] = defaultdict(int)
        # counts_km1 is the frequency table for the "at most k-1 distinct" window [left_km1, r].
        counts_km1: dict[int, int] = defaultdict(int)
        left_k = 0
        left_km1 = 0
        distinct_k = 0
        distinct_km1 = 0
        # Number of distinct values in [left_k, r] that have >= m total occurrences so far.
        good_in_window = 0

        ans = 0

        def update_occurrence(x: int, idx: int) -> None:
            """Update occurrence lists and pos_m / heap; maybe increase good_in_window."""
            nonlocal good_in_window
            dq = occ[x]
            prev_len = len(dq)
            dq.append(idx)
            new_len = prev_len + 1
            if new_len >= m:
                pos = dq[-m]
                pos_m[x] = pos
                heapq.heappush(heap, (pos, x))
                # x just reached m occurrences while already in the k-window.
                if prev_len == m - 1 and counts_k[x] > 0:
                    good_in_window += 1

        def add_to_k_window(x: int) -> None:
            """Extend the 'at most k distinct' window with x."""
            nonlocal distinct_k, good_in_window
            if counts_k[x] == 0:
                distinct_k += 1
                # x enters the window; if it already has >= m occurrences, count it.
                if len(occ[x]) >= m:
                    good_in_window += 1
            counts_k[x] += 1

        def shrink_k_window() -> None:
            """Shrink left_k to keep distinct_k <= k."""
            nonlocal left_k, distinct_k, good_in_window
            while distinct_k > k:
                y = nums[left_k]
                counts_k[y] -= 1
                if counts_k[y] == 0:
                    distinct_k -= 1
                    if len(occ[y]) >= m:
                        good_in_window -= 1
                left_k += 1

        def add_to_km1_window(x: int) -> None:
            """Extend the 'at most k-1 distinct' window with x."""
            nonlocal distinct_km1
            if counts_km1[x] == 0:
                distinct_km1 += 1
            counts_km1[x] += 1

        def shrink_km1_window() -> None:
            """Shrink left_km1 to keep distinct_km1 <= k-1."""
            nonlocal left_km1, distinct_km1
            while distinct_km1 > k - 1:
                y = nums[left_km1]
                counts_km1[y] -= 1
                if counts_km1[y] == 0:
                    distinct_km1 -= 1
                left_km1 += 1

        def current_min_pos() -> Optional[int]:
            """Return the minimum pos_m among values still in the k-window."""
            while heap and (
                pos_m.get(heap[0][1]) != heap[0][0]
                or counts_k[heap[0][1]] == 0
            ):
                heapq.heappop(heap)
            return heap[0][0] if heap else None

        for r, x in enumerate(nums):
            # 1) Update global occurrence info and candidate positions.
            update_occurrence(x, r)

            # 2) Extend both windows with x, then shrink to maintain constraints.
            add_to_k_window(x)
            shrink_k_window()
            add_to_km1_window(x)
            shrink_km1_window()

            # 3) If we have exactly k distinct in the k-window and all of them
            #    already reached >= m occurrences, compute valid left bounds.
            if distinct_k == k and good_in_window == k:
                min_pos = current_min_pos()
                if min_pos is None:
                    continue

                # left in [left_k, left_km1 - 1] gives exactly k distinct;
                # left <= min_pos ensures each of the k values appears at least m times.
                right_j = left_km1 - 1
                if min_pos < left_k:
                    continue
                if right_j >= left_k:
                    right = min(min_pos, right_j)
                    if right >= left_k:
                        ans += right - left_k + 1

        return ans