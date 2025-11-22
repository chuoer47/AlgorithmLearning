# 提取出每一个d

s = input()
mod = 10007


def solution(s):
    size = len(s)
    nums = [s[i:i + 5] for i in range(0, size, 5)]

    # print(nums)

    def helper(nums):
        return [int(x[2:-1]) for x in nums]

    nums = helper(nums)
    # print(nums)

    n = len(nums)
    pi = [nums[0] % mod]
    for i in range(1, n):
        x = nums[i]
        pi.append(pi[-1] * x % mod)
    pi.append(1)
    rpi = [nums[-1] % mod]
    for i in range(n - 2, -1, -1):
        x = nums[i]
        rpi.append(rpi[-1] * x % mod)
    rpi = rpi[::-1]
    rpi.append(1)

    #
    # print(pi, rpi)

    ans = 0
    for i in range(n):
        ans = (ans + pi[i - 1] * rpi[i + 1] % mod) % mod
    return ans


print(solution(s))
