from collections import defaultdict

if __name__ == '__main__':
    n, q = map(int, input().split())
    cnt = defaultdict(int)
    nums = list(map(int, input().split()))
    for x in nums:
        cnt[x] += 1
    pre = sum(nums)

    for _ in range(q):
        ans = 0
        x = int(input())
        if x == 1:
            print(pre)
            continue
        tmp = defaultdict(int)
        for k, v in cnt.items():
            if v > 0:
                ans += v * (k // x)
                tmp[k // x] += v
        cnt = tmp
        pre = ans
        print(ans)
