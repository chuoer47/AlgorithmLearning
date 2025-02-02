class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        # 至多移动一次，就是把一个移动到可以移动的最佳位置，然后判断最大的空闲时间
        # 但是怎么判断出来最佳的移动位置？

        # 找出空闲的区间
        now = 0
        free = []
        for s, e in zip(startTime, endTime):
            if s >= now:
                free.append([now, s, 0])
            free.append([s, e, 1])
            now = e
        if now < eventTime:
            free.append([now, eventTime, 0])

        # print(free)
        # 前后缀分解，找到最大的空闲区域
        last = [[j - i, t] for i, j, t in free]

        n = len(last)

        def getPi(last):
            pi = []
            for i, (time, t) in enumerate(last):
                if t == 0:
                    if i == 0:
                        pi.append(time)
                    else:
                        pi.append(max(time, pi[-1]))
                else:
                    if i == 0:
                        pi.append(0)
                    else:
                        pi.append(pi[-1])
            return pi

        # print(last)

        ans = max(i for i, t in last if t == 0)
        pi = getPi(last)
        rpi = getPi(last[::-1])[::-1]

        # print(pi, rpi)

        for i, (time, t) in enumerate(last):
            if t == 1:
                # 特判
                if i == 0:
                    if i + 2 < n and rpi[i+2] >= time:
                        ans = max(ans,time + last[i+1][0])
                    continue
                elif i == n - 1:
                    if i - 2 >= 0 and pi[i-2] >= time:
                        ans = max(ans,time + last[i-1][0])
                    continue
                # 一般处理
                if (i - 2 >= 0 and pi[i - 2] >= time) or (i + 2 < n and rpi[i + 2] >= time):
                    # 看一下能不能移走
                    ans = max(ans, last[i - 1][0] + last[i + 1][0] + time)
                else:
                    # 能不能移到相邻两边
                    tmp = 0
                    tmp += last[i - 1][0] if last[i - 1][1] == 0 else 0
                    tmp += last[i + 1][0] if last[i + 1][1] == 0 else 0
                    ans = max(ans, tmp)
        return ans