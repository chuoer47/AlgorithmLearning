class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        m = n*n
        v = maxWeight // w
        return min(v,m)