# Definition for a binary tree node.
from cmath import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None, father=None):
        self.val = val
        self.left = left
        self.right = right


# 1.找树的直径，这个需要转化图
# 2.使用官方解答
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf

        def dfs(node):
            if node is None:
                return 0
            l_val = dfs(node.left)
            r_val = dfs(node.right)
            nonlocal ans
            ans = max(ans, l_val + r_val + node.val)
            return max(max(l_val, r_val) + node.val, 0)

        dfs(root)
        return ans
