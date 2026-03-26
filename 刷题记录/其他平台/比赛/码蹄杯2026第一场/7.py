import bisect


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()

    def helper(a, b):
        l = a[0] * b[0]
        r = a[-1] * b[-1]
        val = r

        def check(mid):
            cnt = 0
            for x in a:
                if x > mid:
                    break
                target = int(mid / x)
                cnt += bisect.bisect_right(b, target)
                if cnt >= m:
                    return True
            return False

        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                val = mid
                r = mid - 1
            else:
                l = mid + 1
        ans = []
        for x in a:
            for y in b:
                p = x * y
                if p < val:
                    ans.append(p)
                else:
                    break
        ans.sort()
        if len(ans) < m:
            ans.extend([val] * (m - len(ans)))
        return ans

    return helper(helper(a, b), c)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        nums = main()
        print(*nums)
