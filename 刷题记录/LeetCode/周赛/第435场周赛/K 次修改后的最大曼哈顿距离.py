class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = -inf
        cnt = Counter()
        for i in s:
            cnt[i] += 1
            kk = k

            # Ì°ĞÄ
            ml = min(cnt["N"], cnt["S"])
            mh = min(cnt["W"], cnt["E"])
            nx, ny = abs(cnt["N"] - cnt["S"]), abs(cnt["W"] - cnt["E"])
            ans = nx + ny
            ans += 2 * min(kk, ml)
            kk -= min(kk, ml)
            ans += 2 * min(kk, mh)
            kk -= min(kk, mh)
            res = max(ans, res)

        return res