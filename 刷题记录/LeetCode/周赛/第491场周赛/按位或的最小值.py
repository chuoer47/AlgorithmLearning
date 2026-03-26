class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        # 给定一个数字，判断是否可以通过每行选择一个整数得到的时间复杂度是O(n*m)
        # 但是题目要求是求取最小可能值，同时题目不满足二分性质
        # 假设从最高位开始填，最好的情况就是均为 0
        ans = 0
        n, m = len(grid), len(grid[0])
        mx = max(map(max, grid))
        l = mx.bit_length()

        def check(bit):
            nxt = []
            t = 1 << bit
            for row in grid:
                tmp = [x for x in row if x & t == 0]
                if not tmp:
                    return False, None
                nxt.append(tmp)
            return True, nxt

        for bit in range(l, -1, -1):
            # 判断第bit为能否为0
            flag, nxt = check(bit)
            if flag:
                grid = nxt
            else:
                ans += 1 << bit
        return ans