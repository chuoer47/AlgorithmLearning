class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        nums.sort(reverse=True)
        pi = list(accumulate(nums, initial=0))
        n = len(nums)

        @cache
        def dfs(i, rop1, rop2):
            if i >= n:  # 遍历结束
                return 0
            if rop1 == 0 and rop2 == 0:  # 没有操作机会了
                return pi[-1] - pi[i]
            if rop1 == 0 and nums[i] < k:
                return pi[-1] - pi[i]
            ans = inf
            # 可以应用两次下标
            # 应用一次
            if rop1 > 0:
                ans = min(ans, math.ceil(nums[i] / 2) + dfs(i + 1, rop1 - 1, rop2))
            if rop2 > 0 and nums[i] >= k:
                ans = min(ans, nums[i] - k + dfs(i + 1, rop1, rop2 - 1))
            # 应用两次
            if rop1 > 0 and rop2 > 0:
                if math.ceil(nums[i] / 2) >= k:
                    ans = min(ans, math.ceil(nums[i] / 2) - k + dfs(i + 1, rop1 - 1, rop2 - 1))
                if nums[i] >= k:
                    ans = min(ans, math.ceil((nums[i] - k) / 2) + dfs(i + 1, rop1 - 1, rop2 - 1))
            # 不应用
            ans = min(ans, nums[i] + dfs(i + 1, rop1, rop2))
            return ans

        return dfs(0, op1, op2)