from collections import deque
from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        ans = 0
        n = len(pizzas)
        pizzas.sort()
        q = deque(pizzas)
        for i in range(0,n//4,2):
            ans += q.pop()
            for _ in range(3):
                q.popleft()
        for i in range(1,n//4,2):
            q.pop()
            ans += q.pop()
            for _ in range(2):
                q.popleft()
        return ans