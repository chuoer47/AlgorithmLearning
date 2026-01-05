class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = inf
        l, r = 1, n

        def check(mid):
            # 使用滑动窗口完成
            cnt = Counter()
            value = l = 0
            for r, v in enumerate(nums):
                cnt[v] += 1
                value += v if cnt[v] == 1 else 0
                while r - l + 1 > mid:
                    vv = nums[l]
                    cnt[vv] -= 1
                    value -= vv if cnt[vv] == 0 else 0
                    l += 1
                if r - l + 1 == mid:
                    if value >= k:
                        return True
            return False

        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans if ans < inf else -1
