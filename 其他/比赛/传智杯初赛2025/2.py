T = int(input())


def solution() -> list:
    cnt0 = x
    cnt1 = n - y + 1
    vis = set()
    ans = []

    for i in nums:
        if i not in vis:
            cnt0 -= int(1 <= i <= x)
            cnt1 -= int(y <= i <= n)
            vis.add(i)
        else:
            cnt0 += int(1 <= i <= x)
            cnt1 += int(y <= i <= n)
            vis.remove(i)
        ans.append(f"{cnt0} {cnt1}")
    return ans


for _ in range(T):
    n, m, x, y = map(int, input().split(" "))
    nums = [int(input()) for _ in range(m)]
    ans = solution()
    for x in ans:
        print(x)
