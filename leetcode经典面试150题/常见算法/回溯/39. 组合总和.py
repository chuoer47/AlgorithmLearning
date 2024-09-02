class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        now = []
        s = 0

        def dfs():
            nonlocal s
            if s == target:
                t = now.copy()
                t.sort()
                if t not in ans:
                    ans.append(t)
                return
            if s > target:
                return
            for i in candidates:
                if s + i <= target:
                    s += i
                    now.append(i)
                    dfs()
                    now.pop()
                    s -= i
                else:
                    break

        dfs()
        return ans
