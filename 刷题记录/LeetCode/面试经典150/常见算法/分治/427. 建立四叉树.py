"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r0, c0, r1, c1):
            if all(grid[i][j] == grid[r0][c0] for i in range(r0, r1) for j in range(c0, c1)):
                return Node(grid[r0][c0] == 1, True)
            else:
                return Node(
                    True,
                    False,
                    dfs(r0, c0, (r0 + r1) // 2, (c0 + c1) // 2),
                    dfs(r0, (c0 + c1) // 2, (r0 + r1) // 2, c1),
                    dfs((r0 + r1) // 2, c0, r1, (c0 + c1) // 2),
                    dfs((r0 + r1) // 2, (c0 + c1) // 2, r1, c1)
                )

        return dfs(0, 0, len(grid), len(grid))
