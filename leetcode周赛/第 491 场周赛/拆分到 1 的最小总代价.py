class Solution:
    @cache
    def minCost(self, n: int) -> int:
        if n == 1:
            return 0
        cost = inf
        for i in range(1,n):
            cost = min(cost,i * (n - i) + self.minCost(i) + self.minCost(n - i))
        return cost