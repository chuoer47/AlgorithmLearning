class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # 找出空闲的区间
        now = 0
        free = []
        for s, e in zip(startTime, endTime):
            if s >= now:
                free.append([now, s])
            now = e
        if now < eventTime:
            free.append([now, eventTime])

        last = [j - i for i, j in free]  # 持续时间
        # 滑动窗口，k为单位
        pi = list(accumulate(last, initial=0))
        n = len(pi)
        k = min(k + 1, n - 1)
        ans = 0
        for i in range(k, n):
            ans = max(ans, pi[i] - pi[i - k])
        return ans