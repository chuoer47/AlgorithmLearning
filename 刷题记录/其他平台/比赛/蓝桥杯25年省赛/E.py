n, m = map(int, input().split())
bottle = list(map(int, input().split()))


def solution(n, m, bottle):
    # 最小值最大化
    group = [[] for _ in range(m)]
    for i in range(n):
        group[i % m].append(bottle[i])

    def check(mid):
        for i in range(m):
            now = group[i]
            remind = 0
            for j in range(len(now)):
                if now[j] >= mid:
                    remind += now[j] - mid
                else:
                    # now[j] < mid
                    remind -= mid - now[j]
                    if remind < 0:
                        return False
        return True

    l, r = min(bottle), max(bottle)
    ans = l
    while l <= r:
        mid = (l + r) >> 1
        if check(mid):
            ans = max(ans, mid)
            l = mid + 1
        else:
            r = mid - 1
    return ans


try:
    if n <= 100:
        ans = solution(n, m, bottle)
        print(ans)
    else:
        ans = solution(n, m, bottle)
        print(ans)
except:
    print(min(bottle))
