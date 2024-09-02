"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        from collections import deque
        stack = deque()
        stack.append(root)
        while stack:
            slen = len(stack)
            for i in range(slen):
                now = stack.popleft()
                print(now)
                if now.left is not None:
                    stack.append(now.left)
                if now.right is not None:
                    stack.append(now.right)
                if i == slen - 1:
                    now.next = None
                    continue
                now.next = stack[0]
        return root
