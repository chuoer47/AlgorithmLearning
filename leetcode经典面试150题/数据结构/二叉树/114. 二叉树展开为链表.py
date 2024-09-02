# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if root is None:
                return
            stack.append(root)
            dfs(root.left)
            dfs(root.right)
        stack = []
        dfs(root)
        n = len(stack)
        for i,node in enumerate(stack):
            node.left = None
            if i==n-1:
                node.right = None
            else:
                node.right = stack[i+1]

