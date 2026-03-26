from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def getPi(nums):
            n = len(nums)
            pi = [0] * n
            for i in range(n):
                if nums[i] == k:
                    pi[i] = pi[i - 1] + 1
                else:
                    pi[i] = pi[i - 1]
            return pi
        pi = getPi(nums)
        rpi = getPi(nums[::-1])[::-1]

        # print(pi)
        cnt = [0] * 55
        ans = max(pi)
        for i in range(n):
            v = nums[i]
            if v == k:
                continue
            cnt[v] = max(cnt[v], pi[i]) + 1
            ans = max(ans, cnt[v] + rpi[i])
        # print(cnt)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxFrequency(nums=[2,8], k=8))
