class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # (0,0,0)/(0,1,2)/(1,1,1)/(2,2,2)/
        mapper = [[] for _ in range(3)]
        for v in nums:
            mapper[v % 3].append(v)
        for row in mapper:
            row.sort()
        sn = 0
        for i in range(3):
            if len(mapper[i]) >= 3:
                sn = max(sn, sum(mapper[i][-3:]))
        if all(len(mapper[i]) >= 1 for i in range(3)):
            sn = max(sn, sum(mapper[i][-1] for i in range(3)))
        return sn
