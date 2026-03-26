#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param S int整型一维数组
# @return int整型二维数组
#
from typing import List


class Solution:
    def dfs(self, depth, max_depth, now: List, ans, S):
        if depth == max_depth:
            ans.append(now.copy())
            return
        self.dfs(depth + 1, max_depth, now, ans, S)  # 不加入

        now.append(S[depth])
        self.dfs(depth + 1, max_depth, now, ans, S)  # 加入
        now.pop()

        return

    def subsets(self, S: List[int]) -> List[List[int]]:
        # write code here
        max_depth = len(S)
        if max_depth == 0:
            return []
        ans = []
        self.dfs(0, max_depth, [], ans, S)
        ans.sort(key=lambda x: len(x))
        return ans


if __name__ == '__main__':
    s = Solution()
    S = [1, 2, 3]
    s.subsets(S)
