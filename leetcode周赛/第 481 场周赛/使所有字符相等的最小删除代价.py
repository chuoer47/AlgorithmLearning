class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        sn = defaultdict(int)
        for i,j in zip(s,cost):
            sn[i] += j
        return sum(cost) - max(sn.values())