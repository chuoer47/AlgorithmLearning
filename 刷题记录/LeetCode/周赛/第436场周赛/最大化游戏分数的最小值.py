# 这道题目与我而言 难点主要在怎么写check函数
# 周赛的时候没有想出来
# 只需要贪心 当不足时 来回跳即可
# 跳的时候记录一下后面一个 在前面一个来回跳的时 已经有的数字即可

class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def check(target):
            n = len(points)
            rem = m
            pre = 0
            for i, p in enumerate(points):
                k = (target - 1) // p + 1 - pre
                if i == n - 1 and k <= 0:
                    break
                # 如果不是最后一个数字，不管如何都要继续往后面走，k起码为1
                k = 1 if k < 1 else k
                rem -= k * 2 - 1
                if rem < 0:
                    return False
                pre = k - 1
            return True

        ans = 0
        n = len(points)
        if m < n:
            # 特判即可
            return 0
        l, r = 1, min(points) * (m // 2 + 1)
        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                ans = max(ans, mid)
                l = mid + 1
            else:
                r = mid - 1
        return ans
