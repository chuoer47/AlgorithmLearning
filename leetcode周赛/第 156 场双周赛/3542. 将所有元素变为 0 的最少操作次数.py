from cmath import inf
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 可能是一个单调栈的问题
        st = []
        ans = 0
        for x in nums + [-inf]:
            while st and st[-1] >= x:
                t = st.pop()
                if t > x and t != 0:
                    ans += 1
            st.append(x)

        return ans
