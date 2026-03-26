class BSTIterator:
    heap = []

    def __init__(self, root: Optional[TreeNode]):
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            self.heap.append(node.val)
            dfs(node.right)

        dfs(root)

    def next(self) -> int:
        return self.heap.pop(0)

    def hasNext(self) -> bool:
        return self.heap != []