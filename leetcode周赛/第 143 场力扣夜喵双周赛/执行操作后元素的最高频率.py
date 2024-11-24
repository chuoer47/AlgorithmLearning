from collections import Counter
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = Counter(nums)
        nums_sorted = sorted(set(nums))  # 排序后的唯一元素列表
        n = len(nums_sorted)

        # 辅助函数，用于二分查找左侧边界
        def find_left_boundary(i, diff):
            left, right = 0, i - 1
            while left <= right:
                mid = (left + right) // 2
                if nums_sorted[i] - nums_sorted[mid] <= diff:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        # 辅助函数，用于二分查找右侧边界
        def find_right_boundary(i, diff):
            left, right = i + 1, n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums_sorted[mid] - nums_sorted[i] <= diff:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        # 预处理每个元素能够覆盖的其他元素的范围
        left = [0] * n
        right = [0] * n
        k2left = [0] * n
        k2right = [0] * n

        # 构建前缀和数组
        prefix_sum = [0] * (n + 1)
        for i, num in enumerate(nums_sorted):
            prefix_sum[i + 1] = prefix_sum[i] + cnt[num]

        # 使用二分查找找到边界
        for i in range(n):
            left[i] = find_left_boundary(i, k)
            right[i] = find_right_boundary(i, k)
            k2left[i] = find_left_boundary(i, 2 * k)
            k2right[i] = find_right_boundary(i, 2 * k)

        # 注意：由于二分查找返回的是索引，且我们的边界是包含/不包含的形式，
        # 因此 left[i] 不需要调整，但 right[i] 需要减 1 来变成不包含的形式。
        # 然而，由于我们在计算范围时使用的是 [left[i], right[i] + 1) 的形式，
        # 所以这里 right[i] 不需要额外减 1，它会自然地在计算范围时被处理。

        ans = 0
        for i in range(n):
            # 当前元素的出现次数
            now = cnt[nums_sorted[i]]

            # 使用前缀和计算 other_count
            other_count = prefix_sum[right[i] + 1] - prefix_sum[left[i]] - now

            # 使用前缀和计算 k2l 和 k2r（注意要调整索引以匹配前缀和数组）
            k2l = prefix_sum[i + 1] - prefix_sum[k2left[i]]
            # 注意：这里 k2right[i] + 1 可能等于 n，但前缀和数组已经处理了这种情况。
            k2r = prefix_sum[k2right[i] + 1] - prefix_sum[i]

            # 更新当前元素的出现次数（考虑操作次数限制）
            now_with_operations = now + min(other_count, numOperations)
            k2l_with_operations = min(k2l, numOperations)
            k2r_with_operations = min(k2r, numOperations)
            # print(k2l_with_operations, k2r_with_operations)

            # 更新答案
            ans = max(ans, now_with_operations, k2l_with_operations, k2r_with_operations)

        return ans
