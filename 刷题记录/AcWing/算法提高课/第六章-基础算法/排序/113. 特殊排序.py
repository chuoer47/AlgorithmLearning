"""
https://www.acwing.com/problem/content/115/
这是一道交互题目
"""


def compare():
    pass


class Solution(object):
    def specialSort(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        ans = [1]
        for i in range(2, N+1):
            # 每次寻找
            l, r = 0, len(ans)
            while l < r:
                mid = (l + r) >> 1
                if compare(ans[mid], i):
                    l = mid + 1
                else:
                    r = mid
            ans.insert(l,i)
        return ans
