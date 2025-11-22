from functools import cache


def helper(num: int) -> int:
    nums = str(num)
    n = len(nums)

    @cache
    def dfs(i, is_limit, is_num, p1, p2):
        if i == n:
            return 0
        ans = 0
        hi = int(nums[i]) if is_limit else 9
        for d in range(0, hi + 1):

            if p1 is not None and p2 is not None:
                if p1 > max(d, p2) or p1 < min(d, p2):
                    ans += 1
            pp1, pp2 = d, p1
            if not is_num and d == 0:
                pp1 = pp2 = None

            ans += dfs(i + 1, is_limit and d == hi, is_num or d > 0, pp1, pp2)
        return ans

    return dfs(0, True, False, None, None)


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return helper(num2) - helper(num1 - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.totalWaviness(num1=120, num2=130))
    print(s.totalWaviness(num1=198, num2=202))
    # print(s.totalWaviness(1, 100000))
