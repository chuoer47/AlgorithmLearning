class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        ldp = [inf] * n
        rdp  = [inf] * n

        ldp[0] = ans = 0
        for idx, x in restrictions:
            ldp[idx] = rdp[idx] = x
        for i in range(1, n):
            ldp[i] = min(ldp[i - 1] + diff[i - 1], ldp[i])
        for i in range(n - 2,-1,-1):
            rdp[i] = min(rdp[i + 1] + diff[i],rdp[i])
        ans = 0
        for l,r in zip(ldp,rdp):
            ans = max(ans,min(l,r))
        # print(ldp,rdp)
        return ans