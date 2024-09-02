class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        now = []
        def dfs(n_depth):
            if len(now)==k:
                ans.append(now.copy())
                return
            if n_depth>n:
                return
            now.append(n_depth)
            dfs(n_depth+1)
            now.pop()

            dfs(n_depth+1)
        dfs(1)
        return ans