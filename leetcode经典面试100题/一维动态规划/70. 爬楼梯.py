"""
https://leetcode.cn/problems/climbing-stairs/
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        now, passOne, passTwo = 0, 1, 0
        for i in range(n):
            now = passOne+passTwo
            passOne, passTwo = now, passOne
        return now

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))