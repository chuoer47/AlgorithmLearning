class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        # 一次遍历
        ans = None
        x0,y0 = center
        for x,y,q in towers:
            if abs(x - x0) + abs(y - y0) <= radius:
                if not ans or q > ans[2] or (q == ans[2] and [x,y] < ans[:2]):
                    ans = [x,y,q]
        return ans[:2] if ans else [-1,-1]