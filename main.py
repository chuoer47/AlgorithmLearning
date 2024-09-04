# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from heapq import *
from typing import Optional, List


class Solution:
    List.__lt__ = lambda a,b : a.val < b.val
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [node for node in lists if node]
        heapify(heap)

        ans = ListNode()
        tail = ans
        while heap:
            val, node = heappop(heap)
            tail.next = node
            node = node.next
            if node:
                heappush(heap, (node.val, node))
        return ans.next
