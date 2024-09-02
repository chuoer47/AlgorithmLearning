class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(pos_left, pos_right, in_left, in_right):
            if pos_left > pos_right:
                return None
            p_root = pos_right
            in_root = dic[postorder[p_root]]
            root = TreeNode(postorder[p_root])
            size_left_subtree = in_root - in_left

            root.left = dfs(pos_left, pos_left + size_left_subtree - 1, in_left, in_root - 1)
            root.right = dfs(pos_left + size_left_subtree, pos_right - 1, in_root + 1, in_right)
            return root

        n = len(inorder)
        dic = {v: i for i, v in enumerate(inorder)}
        return dfs(0, n - 1, 0, n - 1)