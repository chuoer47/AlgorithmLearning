ListNode.__lt__ = lambda a,b : a.val < b.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [node for node in lists if node]
        heapify(heap)

        ans = ListNode()
        tail = ans
        while heap:
            node = heappop(heap)
            tail.next = node
            tail = tail.next
            node = node.next
            if node:
                heappush(heap, node)
        return ans.next
