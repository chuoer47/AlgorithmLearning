from typing import List

from sortedcontainers import SortedList, SortedSet


class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        s = list(s)
        st = []
        for i, x in enumerate(s):
            if not st or s[st[-1]] != x:
                st.append(i)
        sl = SortedSet(st)
        ans = []
        n = len(s)

        def helper(l, r):

            lidx = sl.bisect_right(l) - 1
            ridx = sl.bisect_right(r) - 1
            # print(l,r,sl,lidx,ridx)
            return r - l + 1 - (ridx - lidx + 1)

        for q in queries:
            if len(q) == 2:
                j = q[1]
                s[j] = "B" if s[j] == "A" else "A"
                # 分类讨论？
                if j + 1 < n:
                    if s[j + 1] == s[j]:
                        sl.remove(j + 1)
                        sl.add(j)
                    else:
                        sl.add(j + 1)
                        sl.add(j)
                if j - 1 >= 0:
                    if s[j - 1] == s[j]:
                        sl.remove(j)
                    else:
                        sl.add(j)
                # print(sl)
            else:
                l, r = q[1:]
                ans.append(helper(l, r))
        return ans
