# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(pl, pr, il, ir):
            if pl > pr:
                return None
            p_root = pl
            in_root = dic[preorder[p_root]]
            root = TreeNode(preorder[p_root])
            size_left_subtree = in_root - il

            root.left = dfs(pl + 1, pl + size_left_subtree, il, in_root - 1)
            root.right = dfs(pl + size_left_subtree + 1, pr, in_root + 1, ir)
            return root

        n = len(preorder)
        dic = {v: i for i, v in enumerate(inorder)}
        return dfs(0, n - 1, 0, n - 1)